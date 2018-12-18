############################################################
#               PART 1
############################################################
def sumFreq(inputFile):
    # yield sum(map(int, inputFile))
    total = sum(map(int, inputFile))
    print(total)

############################################################
#               PART 2
############################################################

def repeatedFrequency(inputFile):
    frequency = 0
    frequencylist = set()
    data = list(map(int, inputFile))
    found = True
    while found:
        for i in data:
            if frequency in frequencylist:
                print(frequency)
                found = False
                break
            frequencylist.add(frequency)
            frequency += i


def main():
    f = open('input.txt', 'r')
    # sumFreq(f)
    repeatedFrequency(f)

main()