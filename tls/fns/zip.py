def zipfaiData():
    from sys import path
    path.append('..')

    from json import loads
    from tls.ipts.ct import gtFlCt
    from tls.fns.dicts import merge_dicts
    path.remove('..')
    from collections import Counter

    count = gtFlCt()

    fls = [] # empty arr to store which files need to be analyzed
    fl = [] # empty arr to combine json files
    for x in range(int(count)):
        fls.append('../data/' + input('Enter the name of the file in the "data" folder (i.e. Othello.json): ')) # append the file names into an array
        fl.append(loads(open(fls[x]).read())) # append the contents of the jsons into a list
    fl = sum(fl, []) # combine the nested lists into a single list
    fl = dict(Counter(fl)) # count the number of occurences of the words
    
    return fl, fls
