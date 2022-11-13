def zipfaiData():
    from sys import path
    path.append('..')

    from json import loads
    from tls.ipts.ct import gtFlCt
    from tls.fns.dicts import merge_dicts
    path.remove('..')
    from collections import Counter

    fls = [] # empty arr to store which files need to be analyzed
    fl = [] # empty arr to combine json files

    info = gtFlCt()
    files, fileCt =  list(info)
    
    if fileCt == "a":
        b = 0
        for j in files:
            fls.append('../data/' + j)
            fl.append(loads(open(fls[b]).read()))
            b += 1
    else:
        for x in range(int(fileCt)):
            fls.append('../data/' + input('Enter the name of the file in the "data" folder (i.e. Othello.json): ')) # append the file names into an array
            fl.append(loads(open(fls[x]).read())) # append the contents of the jsons into a list
    fl = sum(fl, []) # combine the nested lists into a single list
    fl = dict(Counter(fl)) # count the number of occurences of the words
    
    return fl, fls
