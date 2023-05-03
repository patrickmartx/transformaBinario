from utils.files import readFile
from utils.binary import binaryToDecimalSM, sumBinSM, subtractBinSM, binaryToDecimalC2, sumBinC2, subtractBinC2

values = readFile('entrada.txt')

sm_to_decimal = binaryToDecimalSM(values)

binarySumSM = sumBinSM(values)
binarySubtractSM = subtractBinSM(values)
operations = [binarySumSM, binarySubtractSM]
decimalOp = binaryToDecimalSM(operations)

c2_to_decimal = binaryToDecimalC2(values)

binarySumC2 = sumBinC2(values)
binarySubtractC2 = subtractBinC2(values)
operations2 = [binarySumC2, binarySubtractC2]
decimalOp2 = binaryToDecimalC2(operations2)




# prints

for index in sm_to_decimal:
    print(index)
print()
for index in operations:
    print(index)
print()
for index in decimalOp:
    print(index)
print()

for index in c2_to_decimal:
    print(index)
print()
for index in operations2:
    print(index)
print()
for index in decimalOp2:
    print(index)
