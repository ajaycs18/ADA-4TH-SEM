arr = list(map(int, input("enter array of numbers: ").split()))

# pythonic way    
sumEvenBitDigits = sum([digit for digit in arr if bin(digit)[2:].count('1') % 2 == 0])
print(sumEvenBitDigits)

# normal way
def isEven1Bits(num):
    one_count = 0
    while num:
        one_count += num & 1
        num >>= 1
    return one_count % 2 == 0

sumEvenBitDigits = 0
for digit in arr:
    if isEven1Bits(digit):
        sumEvenBitDigits += digit
print(sumEvenBitDigits)
