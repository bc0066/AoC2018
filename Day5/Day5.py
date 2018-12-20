from pprint import pprint
#############################################################################
#                           PART 1
#############################################################################
def part1(f):
    input1 = f.readline()
    acc = ""
    for x in input1:
        if not acc:
            acc = x
        elif abs(ord(x)-ord(acc[-1])) == 32:
            acc = acc[:-1]
        else:
            acc = acc + x
    print(len(acc))
#############################################################################
#                           PART 2
#############################################################################
def part2(f):
    f.seek(0)
    minVal = 50000
    input2 = f.readline()
    for i in range(ord('A'), ord('Z')+1):
        filteredInput = input2.replace(chr(i), '').replace(chr(i+32), '')
        acc = ""
        for x in filteredInput:
            if not acc:
                acc = x
            elif abs(ord(x)-ord(acc[-1])) == 32:
                acc = acc[:-1]
            else:
                acc = acc + x
        if len(acc) < minVal:
            minVal = len(acc)
    print(minVal)

def main():
    f = open("Day5.txt", 'r')
    part1(f)
    part2(f)

if __name__ == '__main__':
    main()

