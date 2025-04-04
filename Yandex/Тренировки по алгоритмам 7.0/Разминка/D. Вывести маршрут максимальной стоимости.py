n, m = map(int, input().split())

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
route = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j, val in enumerate(map(int, input().split()), 1):
        if dp[i-1][j] > dp[i][j-1]:
            dp[i][j] = dp[i-1][j] + val
            route[i][j] = 'D'
        else:
            dp[i][j] = dp[i][j-1] + val
            route[i][j] = 'R'

steps = []
i, j = n, m
while i > 1 and j > 1:
    steps.append(route[i][j])
    if route[i][j] == 'D':
        i -= 1
    else:
        j -= 1
while j > 1:
    steps.append('R')
    j -= 1
while i > 1:
    steps.append('D')
    i -= 1

print(dp[-1][-1])
print(*steps[::-1])
