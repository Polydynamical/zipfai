def gtFlCt():
    count = ''
    from os import listdir
    fileCt = len(listdir('../data')) # get the number of data files in the data directory

    while count == '': # this loop is for obtaining the number of files to analyze
        try:
            count = int(input('Number of data files to analyze: '))
            if count <= 0:
                print('Goodbye!')
                exit(0)
        except ValueError:
            count = ''
        try:
            if count > fileCt:
                print('Error: Too many files')
                count = ''
        except TypeError:
            count = ''
    return count
