# generate a graph based on occurences of words from a json file

from matplotlib.pyplot import subplots, show
from numpy import arange, array
from collections import Counter
from json import loads

def getList(dict):
    return dict.values()

file = '../data/' + input('Enter the name of the file in the "data" folder (i.e. Othello.json): ') # set path to requested data
dataDict = loads(open(file).read()) # read the contents of the data file

srt = dict(Counter(dataDict)) # count number of occurences of words in file TODO: rewrite own counter
srt = getList(srt) # create a list with only the dict values
srt = [int(i) for i in srt] # convert strings to ints
array(srt.sort(reverse=True)) # sort array starting with highest value first

t = arange(len(srt)) # x values for word occurences
fig, ax = subplots() # initalize matplotlib
# ax.set_yscale('log') # set to allow logarathmic graphs
ax.plot(t, srt) # plot the values

title = file[8:].split('.')[0] + ', Zipfaied' # set the title of the image
ax.set(xlabel='Word', ylabel='Occurences', title=title) # Label the axes and the title
ax.grid() # add a grid to the graph

show() # show the graph in a pop-up window
