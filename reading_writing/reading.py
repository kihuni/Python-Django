files = open('./countries.txt', 'r')
for lines in files.readlines():
    print(lines)
files.close