import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import sys
import numpy as np

# First step - plot and display NFL player data by position. We would like to
# first just display the data properly as a test, then move on to creating a 
# more interactive command line experience to allow the user to supply the position
# of interest. 

# We need to segment our data based on position. Slice table to store relevant info.

# 1976 is the year the Seahawks and Bucs moved into the NFL.

def position_slice(df,pos=str(sys.argv[1])):
	# Selecting rows from df where col == user input
	by_pos = df.loc[df['Pos']==pos]
	return by_pos

def averages_by_pos(s,pos=str(sys.argv[1])):
	if(pos=='WR'):
		return s['Rec':'RcLng'].append(s[:'Seasons'])
	elif(pos=='QB'):
		return s['Patt':'Sk'].append(s[:'Seasons'])
	elif(pos=='RB'):
		return s['Seasons','Ratt':'RLng'].append(s[:'Seasons'])
	else:
		print("Sorry, you entered an invalid position.")
		return

def get_axes(pos=str(sys.argv[1])):
	print("Enter the stat you would like to keep track of.")
	if(pos=='WR'):
		return input("Type one of the following: 'Rec','RcYds','RcTD'.")
	elif(pos=='QB'):
		return input("Type one of the following: 'Patt','PYds','PTD'.")
	elif(pos=='RB'):
		return input("Type one of the following: 'Ratt','Ryds','RTD'.")


def plot_data(data,stat):
	max_seasons = 0;
	#iterate over each row of our dataframe
	for index,row in data.iterrows():
		x = [0,row['Seasons']]
		y = [0,row[stat]]
		plt.plot(x,y,label=row['Player'])

	plt.title('Hall of Fame '+ str(sys.argv[1])+" 's")
	plt.xlabel('Seasons')
	plt.ylabel(stat)
	plt.legend()
	plt.show()

def main():

	# color_sequence = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c',
 #                  '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5',
 #                  '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f',
 #                  '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5']

	all_data = pd.read_csv("data/nfl_hof_by_pos.csv")
	pos_data = position_slice(all_data)
	average = averages_by_pos(pos_data.mean())
	stat = get_axes()

	print(average)

	plot_data(pos_data,stat)

if __name__ == "__main__":
	main()