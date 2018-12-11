import matplotlib as plt
import pandas as pd
import sys

# First step - plot and display NFL player data by position. We would like to
# first just display the data properly as a test, then move on to creating a 
# more interactive command line experience to allow the user to supply the position
# of interest. 


test = pd.read_csv("data/nfl_hof_by_pos.csv")
print(test['WR'])
