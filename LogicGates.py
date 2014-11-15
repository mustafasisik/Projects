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
    for x in line[:inputCount]:
        gates.append(["I", int(x)])
    for x in line[inputCount:]:
        gates.append([x, []])
    for line in text:
        l = line.split()
        for x in l[1:]:
            gates[int(x)][1].append(int(l[0]))
    pprint(gates)
    print " "
    return gates


def andGate(data1, data2):
    return 1 if (data1, data2) == (1, 1) else 0


def orGate(data1, data2):
    return 1 if 1 in (data1, data2) else 0


def notGate(data1):
    return 1 if data1 == 0 else 0


def xorGate(data1, data2):
    return 1 if data1 != data2 else 0


def outputs(data):
    return data


def inputs(data):
    return data


#calling functions as dictionary elements it is helpful for using one line calling a number of if conditions
d = {"A": andGate,
     "R": orGate,
     "N": notGate,
     "X": xorGate,
     "O": outputs,
     "I": inputs}


def traverse(data):
    result = []
    for idx, e in enumerate(data):
        print d[e[0]](data[e[1]])
    return result


pprint(traverse(readline(text)))
