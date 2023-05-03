def binaryToDecimal(values, base=32):
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


def tratarNegativo(val):
    switch = ""
    for i in range(0, len(val)):
        if val[i] == "0":
            switch += "1"
        elif val[i] == "1":
            switch += "0"
    return switch


def somar(val1, val2, base=32):
    val1 = val1[::-1]
    val2 = val2[::-1]
    valResulado = ''
    carry = False
    for i in range(0, base):
        if carry:
            if val1[i] == val2[i] == "0":
                valResulado += "1"
                carry = False
            elif (val1[i] == "1" and val2[i] == "0") or (val1[i] == "0" and val2[i] == "1"):
                valResulado += "0"
                carry = True
            else:
                valResulado += "1"
                carry = True
        else:
            if val1[i] == val2[i] == "0":
                valResulado += "0"
                carry = False
            elif (val1[i] == "1" and val2[i] == "0") or (val1[i] == "0" and val2[i] == "1"):
                valResulado += "1"
                carry = False
            else:
                valResulado += "0"
                carry = True
    return valResulado[::-1]


def subtrair(val1, val2, base=32):
    val1 = val1[::-1]
    val2 = val2[::-1]
    valResulado = ''
    carry = False
    for i in range(0, base):
        if carry:
            if val1[i] == val2[i] == "0":
                valResulado += "0"
                carry = True
            elif val1[i] == val2[i] == "1":
                valResulado += "0"
                carry = True
            elif val1[i] == "1" and val2[i] == "0":
                valResulado += "0"
                carry = False
            else:
                valResulado += "0"
                carry = True
        else:
            if val1[i] == val2[i] == "0":
                valResulado += "0"
                carry = False
            elif val1[i] == val2[i] == "1":
                valResulado += "0"
                carry = True
            elif val1[i] == "1" and val2[i] == "0":
                valResulado += "1"
                carry = False
            else:
                valResulado += "0"
                carry = True
    return valResulado[::-1]

def sumBin(value):
    sinal1 = value[0][0]
    sinal2 = value[1][0]

    if sinal1 == sinal2:
        # (positivo + positivo) ou (negativo + negativo)
        valResultado = somar(value[0][1:], value[1][1:], base=31)
        valResultado = sinal1 + valResultado
        return valResultado
    else:
        # (positivo + negativo) ou (negativo + positivo)
        valResultado = subtrair(value[0][1:], value[1][1:], base=31)
        compare = binaryToDecimal([value[0][1:], value[1][1:]])
        if compare[0] > compare[1]:
            # positivo maior + negativo menor
            valResultado = sinal1 + valResultado
        else:
            # negativo maior + positivo menor
            valResultado = sinal2 + valResultado
        return valResultado


def subtractBin(value):
    sinal1 = value[0][0]
    sinal2 = value[1][0]
    compare = binaryToDecimal([value[0][1:], value[1][1:]])

    if sinal1 == sinal2 == "0":
        # positivo - positivo
        if compare[0] > compare [1]:
            # positivo maior - positivo menor
            valResulado = subtrair(value[0][1:], value[1][1:], base=31)
            valResulado = "0" + valResulado
            return valResulado
        else:
            # positivo menor - positivo maior
            valResulado = subtrair(value[1][1:], value[0][1:], base=31)
            valResulado = "1" + valResulado
            return valResulado
    elif sinal1 == sinal2 == "1":
        # negativo - negativo
        if compare[0] > compare[1]:
            # negativo maior - negativo menor
            valResultado = subtrair(value[0][1:], value[1][1:], base=31)
            valResultado = "1" + valResultado
            return valResultado
        else:
            # negativo menor - negativo maior
            valResultado = subtrair(value[1][1:], value[0][1:], base=31)
            valResultado = "0" + valResultado
            return valResultado
    elif sinal1 == "0" and sinal2 == "1":
        # positivo - negativo
        valResultado = somar(value[0][1:], value[1][1:], base=31)
        valResultado = sinal1 + valResultado
        """compare = binaryToDecimal([value[0][1:], value[1][1:]])
        if compare[0] > compare[1]:
            valResultado = subtrair(value[0][1:], value[1][1:], base=31)
            valResultado = sinal1 + valResultado
        else:
            valResultado = subtrair(value[1][1:], value[0][1:], base=31)
            valResultado = sinal2 + valResultado"""
        return valResultado
    else:
        # negativo - positivo
        valResultado = somar(value[0][1:], value[1][1:], base=31)
        valResultado = sinal1 + valResultado
        """compare = binaryToDecimal([value[0][1:], value[1][1:]])
        if compare[0] > compare[1]:
            valResultado = somar(value[0][1:], value[1][1:], base=31)
            valResultado = sinal1 + valResultado
        else:
            valResultado = somar(value[0][1:], value[1][1:], base=31)
            valResultado = sinal2 + valResultado"""
        return valResultado