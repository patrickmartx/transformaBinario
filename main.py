from utils.files import readFile
from utils.binary import *


# Leitura do arquivo:
values = readFile('entrada.txt')

# Sinal e Magnitude:
sm_to_decimal = binaryToDecimalSM(values)
smSum = sumBinSM(values)
smSubtract = subtractBinSM(values)
smOperations = [smSum, smSubtract]
smDecimalOp = binaryToDecimalSM(smOperations)

# Complemento a 2:
c2_to_decimal = binaryToDecimalC2(values)
c2Sum = sumBinC2(values)
c2Subtract = subtractBinC2(values)
c2Operations = [c2Sum, c2Subtract]
c2DecimalOp = binaryToDecimalC2(c2Operations)

# prints
# SM
for index in sm_to_decimal:
    print(index)
print()
for index in smOperations:
    print(index)
print()
for index in smDecimalOp:
    print(index)
print()

# C2
for index in c2_to_decimal:
    print(index)
print()
for index in c2Operations:
    print(index)
print()
for index in c2DecimalOp:
    print(index)
