from sys import argv
from pprint import pprint
fileName = argv[1]
text = open(fileName, "r")


firsLine = text.readline().split()
inputCount = int(firsLine[0])
gateCount = int(firsLine[1])
outputCount = int(firsLine[2])


def readline(text):
    line = text.readline().split()
    gates = []
    for x in line:
        gates.append([x])
    for line in text:
        l = line.split()
        for x in l[1:]:
            gates[int(x)].append(int(l[0]))
    return gates


def traverse(data):
    for e in data:
        if len(e) < 2:
            data[data.index(e)] = e[0]
        elif len(e) < 3:
            data[data.index(e)] = d[e[0]](data[e[1]][0])
        else:
            data[data.index(e)] = d[e[0]](data[e[1]][0], data[e[2]][0])
    return data


def andGate(data1, data2):
    if data1 == "1" and data2 == "1":
        return "1"
    else:
        return "0"


def orGate(data1, data2):
    if data1 == "1" or data2 == "1":
        return "1"
    else:
        return "0"


def notGate(data1):
    return "1" if data1 == "0" else "0"


def xorGate(data1, data2):
    return "1" if data1 != data2 else "0"


def getResult(data1):
    return data1


d = {"A": andGate,
     "R": orGate,
     "N": notGate,
     "X": xorGate,
     "O": getResult}


pprint(traverse(readline(text)))

