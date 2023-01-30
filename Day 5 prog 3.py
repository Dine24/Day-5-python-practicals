import math
def perfectSquares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            dp[i] = min(dp[i], dp[i - j*j] + 1)
    return dp[n]

print(perfectSquares(12)) 
print(perfectSquares(13))
print(perfectSquares(1)) 
print(perfectSquares(4)) 
print(perfectSquares(3))
