#!/usr/bin/env python3

filename = 'day1-input.txt'

rawdata = open(filename, 'r').read()
dataset = rawdata.split("\n")

numset = ['0','1','2','3','4','5','6','7','8','9']
values = []
for item in dataset:
    if item.strip() == '':
        continue
    print("string: '%s'" % item)
    leftnum = ""
    for i in range(0,len(item)):
        # print("item: '%s'" % item[i])
        if item[i] in numset:
            leftnum = item[i]
            print("leftnum (%s): %s" % (i,leftnum))
            break

    rightnum = ""
    for i in range(len(item) - 1,-1,-1):
        # print(i)
        if item[i] in numset:
            rightnum = item[i]
            print("rightnum (%s): %s" % (i,rightnum))
            break

    print('string: %s -> %s%s \n' % (item,leftnum,rightnum))
    values += [int('%s%s' % (leftnum,rightnum))]

# print("Values: %s" % values)
total = 0
for value in values:
    total += value

print("Total: %s" % total)


