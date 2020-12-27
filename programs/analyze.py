# Provide detailed analysis of the words in the requested data

from json import loads
from collections import Counter

file = '../data/' + input('Enter the name of the file in the "data" folder (i.e. Othello.json): ') # Set the path to the requested data file
dataDict = loads(open(file).read()) # Read the contents of the requested file

srt = dict(Counter(dataDict)) # Count the occurences of each word in the file

lst = dict(sorted(srt.items(), key=lambda item: item[1])) # Sort the dict based on the occurences of the word
lst = list(lst.items()) # Convert the sorted dict to sorted tuples
first = str(lst[-1]).split(', ')[1].split(')')[0] # get the number of times the most frequent word appears (used to calculate percentage below)

for w in sorted(srt, key=srt.get, reverse=True):
    print(str( ( int(srt[w])*100 )/( int(first)) )[:5] + '%', w, srt[w]) # print percentage or ratio compared to most frequent word, the word, and number of occurences
