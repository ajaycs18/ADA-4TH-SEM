val = list(map(int, input('enter values: ').split())) 
weights = list(map(int, input('enter weights: ').split())) 
bag_weight = int(input('enter bag weight: ')) 

def knapSack(val, weights, bag_weight):
    dp = [[0] * (bag_weight + 1)] * (len(val) + 1)
    for i in range(len(weights) + 1):
        for j in range(bag_weight + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif weights[i - 1] <= j:
                dp[i][j] = max(val[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[len(val)][bag_weight]

print(knapSack(val, weights, bag_weight))
