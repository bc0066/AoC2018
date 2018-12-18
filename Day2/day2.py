################################################
#                   PART 1
################################################
def part1(f):
    checksum = list(map(str, f))
    twoTotal = 0
    threeTotal = 0
    for i in checksum:
        previtems = []
        for j in i:
            if j not in previtems:
                if ((i.count(j) == 3) and (str(3) not in previtems)):
                    threeTotal +=1
                    previtems.append(str(3))

                elif ((i.count(j) == 2) and (str(2) not in previtems)):
                    twoTotal += 1
                    previtems.append(str(2))
                previtems.append(j)
    Total = twoTotal * threeTotal
    print(Total)

################################################
#                   PART 2
################################################
def part2(f):
    boxID = list(map(str,f))
    nextBox = []
    currentBox = []
    answer1 = ''
    test = []
    for i in range(len(boxID)):
        for j in range(len(boxID)):
            currentBox = list(boxID[i])
            nextBox = list(boxID[j])
            test = [x for x, y in zip(currentBox, nextBox) if x == y]
            if len(test) == len(currentBox)-1:
                print(test)
                answer = list(test)
                if len(answer) > len(answer1):
                    answer1 = answer
def main():
    f = open("day2.txt", 'r')
    # part1(f)
    part2(f)


main()