s = list(map(int, input("enter set of numbers: ").split()))
total = int(input('enter sum: '))

def getSubsets(s, i, total, selected=[]):
    if not total:
        print(selected)
        selected = []
        return True
    if i >= len(s):
        return False

    not_using_first = getSubsets(s, i + 1, total, selected)
    selected.append(s[i])
    using_first = getSubsets(s, i + 1, total - s[i], selected) 
    if using_first == False:
        selected.pop()

    return using_first or not_using_first

if getSubsets(s, 0, total):
    print("There is solution")
else:
    print("No solution")
