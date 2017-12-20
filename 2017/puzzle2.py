import numpy as np

input = np.loadtxt('puzzle2input')

def checksum(input):

    checksum = 0

    for row in input:
        checksum += (np.max(row) - np.min(row))

    return print(checksum)

def part2(input):

    checksum = 0

    for row in input:
        found = False
        while not found:
            maxnum = np.argmax(row)
            i = 0
            while i != len(row) and not found:
                if (i != maxnum) and not found:
                    if (row[maxnum] % row[i]) == 0:
                        checksum+= (row[maxnum]/row[i])
                        found = True
                    else:
                        i += 1
                else:
                    i += 1
            row = np.delete(row, maxnum)

    return print(checksum)
