# generate a graph based on occurences of words a file

from matplotlib.pyplot import subplots, show
from numpy import arange, array
from collections import Counter
from json import loads

def getList(dict):
    return dict.values()

file = input('Enter the path to the file (i.e. data/Othello.json): ')
stuff = loads(open(file).read())

srt = dict(Counter(stuff))
srt = getList(srt)
srt = [int(i) for i in srt]
array(srt.sort(reverse=True))

# Data for plotting
t = arange(len(srt))

fig, ax = subplots()
# ax.set_yscale('log') # set to allow logarathmic graphs

ax.plot(t, srt)

title = file.split(r'/')[1].split('.')[0]

ax.set(xlabel='Word', ylabel='Occurences',
        title='Othello, Zipfaied: ')
ax.grid()

fig.savefig("graph.png")
show()
