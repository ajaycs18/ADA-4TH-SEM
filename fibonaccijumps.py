def genFib(n):
    first, second, third = 0, 1, 1
    while third <= n:
        yield third
        first, second = second, third
        third = first + second

arr = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
n = len(arr)
fibs = list(genFib(n))

# greedy
# jumps = 0
# pos = -1
# while pos < n:
#     for step in reversed(fibs):
#         if pos + step == n or (pos + step < n and arr[pos + step] == 1):
#             jumps += 1
#             pos += step
#             break;
# print(f'final pos: {pos} jumps: {jumps}')

# dynamic programming
jumps = [n] * (n + 1)
arr += [1] # add end jumpable index
for i in range(n + 1):
    if arr[i] == 1:
        for fib in fibs:
            if i - fib == -1:
                jumps[i] = 1
            elif i - fib > -1:
                jumps[i] = min(jumps[i], jumps[i - fib] + 1)
print(f'jumps taken through dp: {jumps[n]}')
