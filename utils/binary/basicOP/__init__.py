def binSum(val1, val2, base=32):
    val1 = val1[::-1]
    val2 = val2[::-1]
    valResult = ''
    carry = False
    for i in range(0, base):
        if carry:
            if val1[i] == val2[i] == "0":
                valResult += "1"
                carry = False
            elif (val1[i] == "1" and val2[i] == "0") or (val1[i] == "0" and val2[i] == "1"):
                valResult += "0"
                carry = True
            else:
                valResult += "1"
                carry = True
        else:
            if val1[i] == val2[i] == "0":
                valResult += "0"
                carry = False
            elif (val1[i] == "1" and val2[i] == "0") or (val1[i] == "0" and val2[i] == "1"):
                valResult += "1"
                carry = False
            else:
                valResult += "0"
                carry = True
    return valResult[::-1]


def binSubtract(val1, val2, base=32):
    val1 = val1[::-1]
    val2 = val2[::-1]
    valResult = ''
    carry = False
    for i in range(0, base):
        if carry:
            if val1[i] == val2[i] == "0":
                valResult += "1"
                carry = True
            elif val1[i] == val2[i] == "1":
                valResult += "1"
                carry = True
            elif val1[i] == "1" and val2[i] == "0":
                valResult += "0"
                carry = False
            else:
                valResult += "1"
                carry = True
        else:
            if val1[i] == val2[i] == "0":
                valResult += "0"
                carry = False
            elif val1[i] == val2[i] == "1":
                valResult += "0"
                carry = False
            elif val1[i] == "1" and val2[i] == "0":
                valResult += "1"
                carry = False
            else:
                valResult += "1"
                carry = True
    return valResult[::-1]

'''def binSubtract(val1, val2, base=32):
    val1 = val1[::-1]
    val2 = val2[::-1]
    valResult = ''
    carry = False
    for i in range(0, base):
        if carry:
            if val1[i] == val2[i] == "0":
                valResult += "0"
                carry = True
            elif val1[i] == val2[i] == "1":
                valResult += "0"
                carry = True
            elif val1[i] == "1" and val2[i] == "0":
                valResult += "0"
                carry = False
            else:
                valResult += "0"
                carry = True
        else:
            if val1[i] == val2[i] == "0":
                valResult += "0"
                carry = False
            elif val1[i] == val2[i] == "1":
                valResult += "0"
                carry = True
            elif val1[i] == "1" and val2[i] == "0":
                valResult += "1"
                carry = False
            else:
                valResult += "0"
                carry = True
    return valResult[::-1]'''
