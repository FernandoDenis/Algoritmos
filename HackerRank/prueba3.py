operations = [
    "1 1",
    "1 44",
    "3",
    "3",
    "2",
    "3",
    "3",
    "1 3",
    "1 37",
    "2",
    "3",
    "1 29",
    "3",
    "1 73",
    "1 51",
    "3",
    "3",
    "3",
    "1 70",
    "3",
    "1 8",
    "2",
    "1 49",
    "1 56",
    "1 81",
    "2",
    "1 59",
    "1 44",
    "2",
    "3",
    "3",
    "2",
    "3",
    "3",
    "1 4",
    "3",
    "1 89",
    "2",
    "1 37",
    "1 50",
    "1 64",
    "2",
    "1 49",
    "1 35",
    "1 85",
    "3",
    "1 41",
    "2",
    "3",
    "3",
    "1 86",
    "3",
    "1 60",
    "1 8",
    "3",
    "1 100",
    "3",
    "1 83",
    "3",
    "1 47",
    "2",
    "1 78",
    "2",
    "1 55",
    "1 97",
    "2",
    "3",
    "1 40"
]


def getMax(operations):
    stack = []
    result = []
    
    maximum = []
    
    for i in operations:
        if i[0] == "1":
            stack.append(i[2:])
            if (len(maximum) == 0 or int(maximum[-1]) <= int(i[2:])):
                maximum.append(i[2:])
        elif i[0] == "2":
            if stack.pop() == maximum[-1]:
                maximum.pop()
        elif i[0] == "3":
            result.append(maximum[-1])
            
    return result
        
print(getMax(operations))
