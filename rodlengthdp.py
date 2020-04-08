length = int(input('enter length: '))
prices = [int(price) for price in input('enter prices: ').split()]
prices.insert(0, 0)
dp = [0] * (length + 1)

for curr_l in range(length + 1):
    for l in range(length + 1):
        if l <= curr_l:
            dp[curr_l] = max(dp[curr_l], prices[l] + dp[curr_l - l])

print(dp[-1])
