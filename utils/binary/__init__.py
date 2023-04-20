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


def sumOp(val1, val2, base=32):
    valResulado = ''
    val3 = ["0"]
    for i in range(0, base - 1):
        # Caso onde os dois binários comparados são 0
        if val1[i] == val2[i] == val3[i] == "0":
            valResulado += "0"
            val3.append("0")
        # Caso onde os dois binários comparados são 0 e o valor anterior tinha dado 10
        elif val1[i] == val2[i] == "0" and val3[i] == "1":
            valResulado += "1"
            val3.append("0")
        # Caso onde: o primeiro bininário seja um e o segundo seja zero ou o primeiro seja zero e o segundo seja um, mas o anterior resultou em 10
        elif (val1[i] == val3[i] == "1" and val2[i] == "0") or (val2[i] == val3[i] == "1" and val1[1] == "0"):
            valResulado += "1"
            val3.append("0")
        # Caso apenas um dos valores comparado seja um, e o anterior não tenha resultado em 10.
        elif (val1[i] == val3[i] == "0" and val2[i] == "1") or (val2[i] == val3[i] == "0" and val1[1] == "1"):
            valResulado += "1"
            val3.append("0")
        # Caso onde os valores comparados ambos são 1, e o anterior não resultou em 10.
        elif val1[i] == val2[i] == "1" and val3[i] == "0":
            valResulado += "0"
            val3.append("1")
        # Caso onde os valores comparados ambos são 1, e o anterior resultou em 10.
        elif val1[i] == val2[i] == val3[i] == "1":
            valResulado += "0"
            val3.append("1")
    return valResulado[::-1]


def tratarNegativo(val):

    return None

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
