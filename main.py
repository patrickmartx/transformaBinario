from utils.files import readFile
from utils.binary import binaryToDecimal, sumbin, subtractbin

values = readFile('entrada.txt')
decimal = binaryToDecimal(values)
binarySum = sumbin(values)
binarySubtract = subtractbin(values)

print('')
for index in values:
    print(index)
print()
for index in decimal:
    print(index)
print()
print(binarySum)
