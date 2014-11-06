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
    data = []
    d = {"input": [], "result": None, "gate": None, "directions": []}
    for x in line[:inputCount]:
        d["result"] = x
        data.append(d)
        d = {"input": [], "result": None, "gate": None, "directions": []}
    for x in line[inputCount:]:
        d["gate"] = x
        data.append(d)
        d = {"input": [], "result": None, "gate": None, "directions": []}

    for line in text:
        data[int(line.split()[0])]["directions"] = [int(x) for x in line.split()[1:]]
    return data


def traverse():
    data = readline(text)
    allResults = []
    for element in data:
        for d in element["directions"]:
            data[d]["input"].append(element["result"])
    for element in data:
        if element["gate"] == "A":
            element["result"] = andGate(element["input"])
        elif element["gate"] == "R":
            element["result"] = orGate(element["input"])
        elif element["gate"] == "N":
            element["result"] = notGate(element["input"][0])
        elif element["gate"] == "X":
            element["result"] = xorGate(element["input"])
        if element["result"] != None:
            allResults.append(element["result"])
    for element in data[inputCount:]:
        for d in element["directions"]:
            if element["result"] != None:
                data[d]["input"].append(element["result"])
    for element in data[inputCount+gateCount:]:
        element["result"] = element["input"]
        if element["result"] != None:
            allResults.append(element["result"])


    return allResults


def andGate(data):
    if data[0] == "1" and data[1] == "1":
        return "1"
    else:
        return "0"


def orGate(data):
    if data[0] == "1" or data[1] == "1":
        return "1"
    else:
        return "0"


def notGate(data):
    return "1" if data == "0" else "0"


def xorGate(data):
    return "1" if data[0] != data[1] else "0"


pprint(traverse())
