# generate a graph based on occurences of words from a json file
from sys import path
path.append('..')

from matplotlib.pyplot import subplots, show
from numpy import arange, array
from tls.fns.dicts import getValues
from tls.fns.zip import zipfaiData
from math import log
path.remove('..')

srt = zipfaiData()
files = srt[1]
srt = srt[0]

def get_title():
    a = ''
    for file in files:
        file = file[8:].split('.')[0]
        a = a + file + ', '
    a += '-- Zipfaied'
    return a

srt = getValues(srt) # create a list with only the dict values
srt = [int(i) for i in srt] # convert strings to ints
array(srt.sort(reverse=True)) # sort array starting with highest value first
print(len(srt))
srt = srt[:150]

t = arange(1, len(srt) + 1) # x values for word occurences
for num in t:
    num = log(num)
for val in srt:
    val = log(val)

fig, ax = subplots() # initalize matplotlib
# ax.set_yscale('log') # set to allow logarathmic graphs
ax.plot(t, srt) # plot the values

title = get_title() # set the title of the image
ax.set(xlabel='Word', ylabel='Occurences', title=title) # Label the axes and the title
ax.grid() # add a grid to the graph

show() # show the graph in a pop-up window
