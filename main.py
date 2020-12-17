from json import loads
from collections import Counter
import numpy as np


stuff = loads(open('othello.json').read())

srt = dict(Counter(stuff))


lst = dict(sorted(srt.items(), key=lambda item: item[1]))
lst = list(lst.items())
last = str(lst[-1])
last = last.split(', ')[1]
last = last.split(')')[0]

# print(srt)

# data = list(srt.items())
# arr = np.array(data)

# arr = list(srt.values)

# for key in srt:
#     print("word: %s , occurences: %s" % (key, srt[key]))

# srt = dict(sorted(srt.items(), key=lambda item: item[1]))
for w in sorted(srt, key=srt.get, reverse=True):
    print(w, srt[w], "               ", str(((int(srt[w])*100)/(int(last))))) # print word, number of occurences, and ratio compared to most used word

# print(lst[-1])
# for words in str:
#   if word not in  
