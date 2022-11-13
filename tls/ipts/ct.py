def gtFlCt():
    count = ''
    from os import listdir
    fileCt = len(listdir('../data')) # get the number of data files in the data directory
    files = listdir('../data')
    yield files

    while count == '': # this loop is for obtaining the number of files to analyze
        try:
            count = input('Number of data files to analyze: ')
            if count == 'a' or count == 'A':
                count = 14279
                
            else:
                count = int(count)
            if count <= 0:
                print('Goodbye!')
                exit(0)
        except ValueError:
            count = ''
        try:
            if (count > fileCt) and (count != 14279):
                print('Error: Too many files')
                count = ''
        except TypeError:
            count = ''
    else:
        if count == 14279:
            yield 'a'
        else:
            yield count

