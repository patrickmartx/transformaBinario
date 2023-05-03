from utils.files import readFile
from utils.binary import binaryToDecimal, sumBin, subtractBin

values = readFile('entrada.txt')
decimal = binaryToDecimal(values, base=32)
binarySum = sumBin(values)
binarySubtract = subtractBin(values)
operations = [binarySum, binarySubtract]
decimalOp = binaryToDecimal(operations)


# prints

for index in decimal:
    print(index)
print()
for index in operations:
    print(index)
print()
for index in decimalOp:
    print(index)
