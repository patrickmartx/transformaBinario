def binaryToDecimal(values):
    '''

    :param values:
    :param base:
    :return:
    '''

    decimals = []
    reverseValue = values[:]
    for index in range(0, len(values)):
        num = 0
        sinal = values[index][0]
        reverseValue[index] = values[index][:0:-1]
        for i in range(0, len(reverseValue[index])):
            if reverseValue[index][i] == '1':
                num += 2 ** i
        if sinal == '0':
            decimals.append(num)
        elif sinal == '1':
            decimals.append(num * -1)

    del reverseValue
    return decimals


def sumOp(val1, val2="1" + "0"*31, base=32):
    print("repeticao")
    print("-")
    valResulado = ''
    aux = 0
    for i in range(0, base-1):
        if val1[i] == val2[i] == "0":
            if aux == 1:
                valResulado += "1"
                aux = 0
            else:
                valResulado += "0"
                aux = 0
        elif (val1[i] == "1" and val2[i] == "0") or (val1[i] == "0" and val2[i] == "1"):
            if aux == 1:
                valResulado += "0"
                aux = 1
            else:
                valResulado += "1"
                aux = 0
        elif val1[i] == val2[i] == "1":
            if aux == 1:
                valResulado += "1"
                aux = 1
            else:
                valResulado += "0"
                aux = 1
    return valResulado[::-1]


def tratarNegativo(val):
    newVal = ""
    for char in val:
        if char == "0":
            newVal += "1"
        else:
            newVal += "0"
    newVal = sumOp(newVal[::-1])
    return newVal


def sumbin(value, base=32):
    sinal1 = value[0][0]
    sinal2 = value[1][0]

    #Caso os dois sejam positivo
    if sinal1 == sinal2 == "0":
        result = sinal1 + sumOp(value[0][base:0:-1], value[1][base:0:-1])
        return result
    #Caso o primeiro seja negativo e o segundo positivo
    elif sinal1 == "1" and sinal2 == "0":
        decimal = binaryToDecimal(value)
        tratarNegativo(value[1])
        for i in range(0, len(decimal)):
            if decimal[i] < 0:
                decimal[i] *= -1
        if decimal[0] >= decimal[1]:
            result = sinal1 + sumOp(value[0][base:0:-1], value[1][base:0:-1])
        else:
            result = sinal2 + sumOp(value[0][base:0:-1], value[1][base:0:-1])
        return result
    # Caso o primeiro seja positivo e o segundo negativo
    elif sinal1 == "0" and sinal2 == "1":
        decimal = binaryToDecimal(value)
        for i in range(0, len(decimal)):
            if decimal[i] < 0:
                decimal[i] *= -1
        if decimal[0] >= decimal[1]:
            result = sinal1 + sumOp(value[0][base:0:-1], value[1][base:0:-1])
        else:
            result = sinal2 + sumOp(value[0][base:0:-1], value[1][base:0:-1])
        return result
    # Caso os dois sejam negativos
    else:
        result = sinal1 + sumOp(value[0][base:0:-1], value[1][base:0:-1])
        return result


def subtractbin(value):
    val1 = value[0]
    val2 = value[1]

    '''if val1[0] == '0' and val2[0] == '0':
        print("Os dois valores são pares")
    elif val1[0] == '0' and val2[0] == '1':
        print("Val1 é par e Val2 é impar")
    elif val1[0] == '1' and val2[0] == '0':
        print("Val1 é impar e Val2 é par")
    else:
        print("Os dois valores são ímpares")'''
    return None
