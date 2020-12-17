from json import loads
from collections import Counter
import numpy as np


stuff = loads(open('othello.json').read())

srt = dict(Counter(stuff))

# data = list(srt.items())
# arr = np.array(data)

# arr = list(srt.values)

for key in srt:
    print("word: %s , occurences: %s" % (key, srt[key]))

# for words in str:
#   if word not in  
