## README
- This project visualizes tree planting trends in San Francisco from 1950-2020 using two visualizations:
1. Tree Map
  - Shows where trees were planted across SF neighborhoods.
  - Each tree is plotted as a circle, with its color representing the decade it was planted.
  - Helps visualize spatial patterns in urban forestry.

2. Partitioned Bar Chart (**COMING SOON**)
  - Displays the top 5 most common tree species.
  - Bars show how many trees were planted per decade.
  - Uses the same colors as the map for consistency.
  - Helps analyze which species were popular in different time periods.

### WRITE UP
For this assignment, I explored San Francisco’s tree-planting trends to 
uncover how the city’s urban forestry efforts have evolved over time. The 
visualization focuses on two key aspects: where trees were planted (using a map) 
and what species were most popular (using a heatmap). The map groups tree 
plantings by decade, with each decade assigned a unique color, making it easy to 
see how planting patterns changed across the city. The heatmap dives deeper into 
the data, showing the top 10 most planted species and how their popularity shifted 
over time. 

I made a few changes to the provided post-process.py script to prepare the 
dataset. Trees without planting dates were grouped under “1955>,” since they were 
known to have been planted before that year. I also grouped planting years into 
decades to simplify the timeline and cleaned up the species names to keep only the 
common names, removing any extra metadata. 

For the map, I used color to represent different decades and plotted each 
tree’s location on the map of San Francisco. The transparency of the dots ensures 
that dense areas don’t get too cluttered while still showing hotspots of planting 
activity. The heatmap, on the other hand, uses a blue gradient to show the number 
of plantings for each species by decade. The x-axis represents the decades, while 
the y-axis lists the top 10 species by total plantings, making it easy to compare 
trends. 

I chose these visualizations because they complement each other: the map 
highlights spatial and temporal trends, while the heatmap focuses on species 
diversity. Of course, there are trade-offs. For example, the heatmap leaves out less common species to keep things focused, and grouping by decade smooths over finer details. But these choices help keep the visualizations clear and easy to 
interpret. Overall, the goal was to create something that tells a meaningful story 
about San Francisco’s trees while being visually engaging and easy to understand. 
