from ..basicOP import *


def binaryToDecimalSM(values, base=32):
    decimals = []
    reverseValue = []
    for index in range(0, len(values)):
        num = 0
        reverseValue.append(values[index][:0:-1])
        for i in range(0, len(reverseValue[index])):
            if reverseValue[index][i] == '1':
                num += 2 ** i
        if base == 32:
            sinal = values[index][0]
            if sinal == '0':
                decimals.append(num)
            elif sinal == '1':
                decimals.append(num * -1)
    del reverseValue
    return decimals


def findNegatives(values):
    sinal1 = values[0][0]
    sinal2 = values[1][0]
    valuesC2 = []
    if sinal1 == "1":
        valuesC2.append(modifyNegative(values[0]))
    else:
        valuesC2.append(values[0])
    if sinal2 == "1":
        valuesC2.append(modifyNegative(values[1]))
    else:
        valuesC2.append(values[1])
    return valuesC2


def modifyNegative(val):
    switch = ""
    for i in range(0, len(val)):
        if val[i] == "0":
            switch += "1"
        elif val[i] == "1":
            switch += "0"
    c2negative = binSum(switch, ("0" * 31 + "1"))
    return c2negative


def binaryToDecimalC2(values, base=32):
    decimals = []
    reverseValue = []
    c2 = []

    for index in range(0, len(values)):
        sinal = values[index][0]
        if values[index][0] == "1":
            c2.append(modifyNegative(values[index]))
        else:
            c2.append(values[index])
        num = 0
        reverseValue.append(c2[index][::-1])
        for i in range(0, len(reverseValue[index])):
            if reverseValue[index][i] == '1':
                num += 2 ** i

        if base == 32:
            if sinal == '0':
                decimals.append(num)
            elif sinal == '1':
                decimals.append(num * -1)

    del reverseValue
    return decimals
