from sys import argv
from pprint import pprint
fileName = argv[1]
text = open(fileName, "r")


firsLine = text.readline().split()
inputCount = int(firsLine[0])
gateCount = int(firsLine[1])
outputCount = int(firsLine[2])


def readFile(text):
    line = text.readline().split()
    data = []
    directions = []
    for x in line[:inputCount]:
        data.append([None, x])
    for x in line[inputCount:]:
        data.append([x, None])
    for line in text:
        directions.append([int(x) for x in line.split()][1:])
    data = zip(data, directions)
    return data


def calculate():
    data = readFile(text)
    return data


pprint(calculate())
