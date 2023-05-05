from ..representation import *


def sumBinSM(value):
    sinal1 = value[0][0]
    sinal2 = value[1][0]

    if sinal1 == sinal2:
        # (positivo + positivo) ou (negativo + negativo)
        valResult = binSum(value[0][1:], value[1][1:], base=31)
        valResult = sinal1 + valResult
        return valResult
    else:
        # (positivo + negativo) ou (negativo + positivo)
        valResult = binSubtract(value[0][1:], value[1][1:], base=31)
        compare = binaryToDecimalSM([value[0][1:], value[1][1:]])
        if compare[0] > compare[1]:
            # positivo maior + negativo menor
            valResult = sinal1 + valResult
        else:
            # negativo maior + positivo menor
            valResult = sinal2 + valResult
        return valResult


def subtractBinSM(value):
    sinal1 = value[0][0]
    sinal2 = value[1][0]
    compare = binaryToDecimalSM([value[0][1:], value[1][1:]])

    if sinal1 == sinal2 == "0":
        # positivo - positivo
        if compare[0] > compare[1]:
            # positivo maior - positivo menor
            valResult = binSubtract(value[0][1:], value[1][1:], base=31)
            valResult = "0" + valResult
            return valResult
        else:
            # positivo menor - positivo maior
            valResult = binSubtract(value[1][1:], value[0][1:], base=31)
            valResult = "1" + valResult
            return valResult
    elif sinal1 == sinal2 == "1":
        # negativo - negativo
        if compare[0] > compare[1]:
            # negativo maior - negativo menor
            valResult = binSubtract(value[0][1:], value[1][1:], base=31)
            valResult = "1" + valResult
            return valResult
        else:
            # negativo menor - negativo maior
            valResult = binSubtract(value[1][1:], value[0][1:], base=31)
            valResult = "0" + valResult
            return valResult
    elif sinal1 == "0" and sinal2 == "1":
        # positivo - negativo
        valResult = binSum(value[0][1:], value[1][1:], base=31)
        valResult = sinal1 + valResult
        return valResult
    else:
        # negativo - positivo
        valResult = binSum(value[0][1:], value[1][1:], base=31)
        valResult = sinal1 + valResult
        return valResult


def subtractBinC2(values):
    c2values = values[:]
    if values[0][0] != values[1][0]:
        c2values = findNegatives(c2values)
        valResult = binSum(c2values[0], c2values[1])
        valResult = modifyNegative(valResult)
    else:
        if values[0][0] == "0":
            c2values[1] = modifyNegative(c2values[1])
            valResult = binSum(c2values[0], c2values[1])
        else:
            c2values[0] = modifyNegative(c2values[0])
            valResult = binSum(c2values[0], c2values[1])
            valResult = modifyNegative(valResult)
    return valResult
