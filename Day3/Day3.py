import re
from collections import defaultdict
from pprint import pprint

def parseInput(f):
    parseData=r'#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)'
    data = []
    for line in f:
        match = re.match(parseData, line)
        if match:
            data.append({
                'ID'     : int(match.group(1)),
                'x'      : int(match.group(2)),
                'y'      : int(match.group(3)),
                'width'  : int(match.group(4)),
                'height' : int(match.group(5))
            })
    pprint(data)

def main():
    f = open("Day3.txt", 'r')
    parseInput(f)

if __name__ == '__main__':
    main()