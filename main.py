from utils.files import readFile
from utils.binary import binaryToDecimal, sumBin#, subtractBin

values = readFile('entrada.txt')
decimal = binaryToDecimal(values)
binarySum = sumBin(values)
#binarySubtract = subtractbin(values)

print('')
for index in values:
    print(index)
'''print()
for index in decimal:
    print(index)

print()'''
print(binarySum)
