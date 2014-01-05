f = open('negsen')
numlist = []
for line in f:
    line = line.strip()
    numlist.append(line)
f = open('../senword/negsen.txt')
i = 0
for line in f:
    i += 1
    line = line.strip()
    for tmp in numlist:
        tmpp = "%d" % i
        if tmp == tmpp:
            print line
            break
