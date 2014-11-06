from sys import argv
from pprint import pprint
import math
filename = argv[1]
text = open(filename, "r")

firstLine = text.readline().split()
pointsCount = int(firstLine[0])
neighborsCount = int(firstLine[1])


def createPointList():
    PointList = []
    for line in text.readlines():
        PointList.append((float(line.split()[0]), float(line.split()[1])))
    return PointList


def findDistances():
    distances = {}
    points = createPointList()
    for x1, y1 in points:
        distanceList = []
        for x2, y2 in points:
            distanceList.append((findDistance(x1, y1 x2, y2), x2, y2))
        distances[(x1, y1)] = sorted(distanceList)[1:neighborsCount+1]
    return distances


def findDistance(x1, y1, x2, y2):
    return math.sqrt((y2-y1)*(y2-y1) + (x2-x1)*(x2-x1))


pprint(findDistances())
