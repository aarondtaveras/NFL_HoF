import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import sys

# First step - plot and display NFL player data by position. We would like to
# first just display the data properly as a test, then move on to creating a 
# more interactive command line experience to allow the user to supply the position
# of interest. 

# We need to segment our data based on position. Slice table to store relevant info.

# 1976 is the year the Seahawks and Bucs moved into the NFL.
# We'll begin our record collection there.

def position_slice(df,pos=str(sys.argv[1])):
	# Selecting rows from df where col == user input, and eliminating
	by_pos = df.loc[df['Pos']==pos]
	return by_pos

def averages_by_pos(s,pos=str(sys.argv[1])):
	if(pos=='WR'):
		return s['Rec':'RcLng']
	elif(pos=='QB'):
		return s['Patt':'Sk']
	elif(pos=='RB'):
		return s['Ratt':'RLng']
	else:
		return

def get_axes(pos=str(sys.argv[1])):
	if(pos=='WR'):
		return ['Rec','RcYds','RcTD']
	elif(pos=='QB'):
		return [ 'Patt','PYds','PTD']
	elif(pos=='RB'):
		return [ 'Ratt','Ryds','RTD']

def main():
	all_data = pd.read_csv("data/nfl_hof_by_pos.csv")
	pos_data = position_slice(all_data)
	average = averages_by_pos(pos_data.mean())
	axes = get_axes()

	print(average)
	pos_data.plot.scatter(title='Hall of Fame '+ str(sys.argv[1])+" 's",x=axes[1],y=axes[2],c=['blue'])
	plt.show()

if __name__ == "__main__":
	main()