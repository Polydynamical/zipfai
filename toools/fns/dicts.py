def merge_dicts(*dicts: dict) -> dict: # function to merge two dicts but adding together the duplicates
    d = {}
    for dict in dicts:
        for key in dict:
            try:
                d[key].append(dict[key])
            except KeyError:
                d[key] = [dict[key]]
    for value in d:
        d[value] = sum(d[value])
    
    return d

def getValues(dict: dict) -> list:
    return dict.values()
