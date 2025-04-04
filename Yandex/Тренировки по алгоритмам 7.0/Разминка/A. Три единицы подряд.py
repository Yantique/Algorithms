n = int(input())

dp = [
    [1, 1, 0],
    [2, 1, 1]
]
while len(dp) < n:
    dp.append([sum(dp[-1]), dp[-1][0], dp[-1][1]])
print(sum(dp[n-1]))
