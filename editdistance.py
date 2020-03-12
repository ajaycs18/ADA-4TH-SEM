str1 = input('Enter string 1: ')
str2 = input('Enter string 2: ')

def findEditDistance(str1, str2):
    if not str1:
        return len(str2) 
    elif not str2:
        return len(str1)

    if str1[-1] == str2[-1]:
        return findEditDistance(str1[:-1], str2[:-1])
    
    return 1 + min(findEditDistance(str1[:-1], str2[:-1]), 
                   findEditDistance(str1, str2[:-1]), 
                   findEditDistance(str1[:-1], str2))

print(findEditDistance(str1, str2))
