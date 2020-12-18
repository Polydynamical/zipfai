from json import loads
from collections import Counter
import numpy as np
import matplotlib.pylab as plt


stuff = loads(open('othello.json').read())

srt = dict(Counter(stuff))

# pltt = sorted(srt.items())
# print(pltt)
# x, y =  zip(*pltt)
# for j in pltt:
# plt.plot(x, y)
# plt.show()

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
    print(str( ( int(srt[w])*100 )/( int(last)) )[:5], r"%", w, srt[w], "               ") # print word, number of occurences, and ratio compared to most used word

# print(lst[-1])
# for words in str:
#   if word not in  
