# Simple post-processing script to create a clean subset of tree data
#     - JRz, for personal use and not indended for real-world applications
 
#  NOTE: This is eliminating valid, useful data in lieu of something easier to visualize
#        It's possible that this will mask trends, as it is often VERY likely that missing data are non-randomly distributed (e.g. more missing data pre-1955 in this dataset)

# Simple post-processing script to exclude pre-1955 trees and fix the 'decade' column
import csv
from datetime import datetime

def passes_filter(row):
    # Filter criteria:
    if len(row['qSpecies']) < 3 or 'Tree(s) ::' in row['qSpecies']:
        return False
    elif len(row['Latitude']) < 2 or len(row['Longitude']) < 2:
        return False
    elif len(row['qSiteInfo']) < 1 or row['qSiteInfo'] == ':':
        return False
    else:
        return True

def determine_decade(plant_date):
    try:
        # Parse the PlantDate in the format MM/DD/YY HH:MM
        parsed_date = datetime.strptime(plant_date, "%m/%d/%y %H:%M")
        year = parsed_date.year

        # Adjust for two-digit year parsing
        if year > 2025:  # If year is in the future (e.g., 2055), correct it
            year -= 100

        # Only include trees planted in 1955 or later
        if year < 1955:
            return None

        # Assign to the appropriate decade
        if 1955 <= year <= 1959:
            return "1955-59"
        else:
            return f"{(year // 10) * 10}"
    except ValueError:
        # If PlantDate is missing or invalid, exclude the row
        return None

# Process data and add 'decade' column
data = []
header = []

with open('static/Street_Tree_List-2022-01-30_RAW.csv', 'r') as f:
    reader = csv.DictReader(f)
    header = reader.fieldnames + ['decade']  # Add the new 'decade' column

    for row in reader:
        if passes_filter(row):
            # Determine the decade for each row
            decade = determine_decade(row.get('PlantDate', ''))
            if decade:  # Only include rows with a valid decade
                row['decade'] = decade
                data.append(row)

print(f"Filtered rows: {len(data)}")

# Export to new CSV
with open('static/Street_Tree_List-2022-01-30_FILTERED.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
