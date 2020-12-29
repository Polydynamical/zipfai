# Provide detailed analysis of the words in the requested data
from sys import path
path.append('..')

from json import loads
from collections import Counter
from tls.fns.dicts import merge_dicts
from tls.ipts.ct import gtFlCt


count = gtFlCt()

fls = [] # empty arr to store which files need to be analyzed

for x in range(count):
    fls.append('../data/' + input('Enter the name of the file in the "data" folder (i.e. Othello.json): ')) # append the file names into an array
    exec(f'fl{x} = loads(open(fls[x]).read())') # Read the contents of the requested file(s)
    exec(f'dict{x} = dict(Counter(fl{x}))') # create dict(s) including the occurences of words from the requested file(s)

try:
    if count == 1: # following four lines need to be rewritten - they merge the dicts with hammer and tongs rather than in a loop: TODO
        srt = merge_dicts(dict0)
    elif count == 2:
        srt = merge_dicts(dict0, dict1)
except:
    print('This error should never occur')
    exit(0)

lst = dict(sorted(srt.items(), key=lambda item: item[1])) # Sort the dict based on the occurences of the word
lst = list(lst.items()) # Convert the sorted dict to sorted tuples
first = str(lst[-1]).split(', ')[1].split(')')[0] # get the number of times the most frequent word appears (used to calculate percentage below)

for w in sorted(srt, key=srt.get, reverse=False):
    print(str( ( int(srt[w])*100 )/( int(first)) )[:5] + '%', w, srt[w]) # print percentage or ratio compared to most frequent word, the word, and number of occurences
