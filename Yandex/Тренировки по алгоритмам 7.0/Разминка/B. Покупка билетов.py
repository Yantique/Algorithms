n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

if n == 1:
    print(data[0][0])
elif n == 2:
    print(min(data[0][0] + data[1][0], data[0][1]))
elif n == 3:
    print(min(data[0][0] + data[1][0] + data[2][0], data[0][0] + data[1][1], data[0][1] + data[2][0], data[0][2]))
else:
    dp = [
        data[0][0],
        min(data[0][0] + data[1][0], data[0][1]),
        min(data[0][0] + data[1][0] + data[2][0], data[0][0] + data[1][1], data[0][1] + data[2][0], data[0][2])
    ]

    for i in range(3, n):
        dp.append(min(
            data[i][0] + dp[i-1],
            data[i-1][1] + dp[i-2],
            data[i-2][2] + dp[i-3])
        )
    print(dp[-1])
