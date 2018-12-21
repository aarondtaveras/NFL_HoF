# NFL Hall of Fame
Using Python and data science/visualization to figure out what it takes to make it into the NFL's Hall of Fame based on position and historical data.

# Demo as of 12/21/18: 

# Running the script:
![step1](https://https://github.com/aarondtaveras/NFL_HoF/images/step1.PNG)


# The first stage in this project is to be able to take the statistics of NFL Hall of Famers and plot them using a scatter plot.

This will give us a rough estimate of the type of stats a player would need to achieve Hall of Fame status. The program will receive one command line argument which is the position that the user would like to research. The program will then display the average relevant statistics needed for a player at this position to enter the Hall of Fame, and then plot all current Hall of Fame players on a scatter plot. The positions supported currently are: 'QB', 'RB', 'WR'.

# As of 12/11/18, the first stage is completed.

# The second stage will be to continue to make statistical adjustments to the data in order to create as accurate results as possible.

After plotting our data using a scatter plot, there were some fundamental issues. 
The first issue was that our x-axis logically must be defined by years - a constant integral value that makes it easy to compare the *rate* of our Hall of Famers' success. This is what would allow us to calculate trajectory. 

The second issue is that if our x-axis must be years, then what will be our y-axis? It can't be a static statistic, as some people may care about Touchdowns while others Yards and others Turnovers... there needs to be some flexibility.

So...

# In stage three, I implemented user input to select the desired statistic, and crudely plotted a career trajectory for each player.

Note the usage of the word crudely: this is due to the fact that we were plotting lines using two points, namely the inception of each players' career (0 years in, 0 stats accumulated) and their finishing stats. This creates a line with a constant slope, which is not how sports operates... but it is a start. However, in order to get the most accurate rate of change, we need to have access to year by year statistics per player. Currently, we don't have the database for this - but we do have access to profootball reference's free data. To continue onward to our goal of having the most accurate statistics possible, we'd need to create a **data scraper** for profootball reference in order to access year by year statistics *only* when we need to. 

This would be a huge undertaking, and I am not sure if profootball reference would be okay with this -- however I will reach out to them and ask and in the meantime research what would be next. I'll outline the next few tentative steps of this project:

# 4. Access yearly statistical data player by player.


--- Closing ---

The goal is to remove as much speculation as possible from the equation of deciding whether or not a player, such as Odell Beckham Jr., is on track to become a pro football Hall of Famer or not.

Further steps (if any are taken) will be logged and implemented within this README and throughout the project's files.
