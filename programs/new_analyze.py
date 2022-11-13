my_file = open("all.txt", "r+")
lines = my_file.readlines()
d = {}

for line in lines:
    line_arr = line.split(" ")
    for word in line_arr:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

# sort dict
d = dict(sorted(d.items(), key=lambda x:x[1]))
print(d)

