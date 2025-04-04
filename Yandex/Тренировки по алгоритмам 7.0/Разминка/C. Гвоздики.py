n = int(input())
arr = sorted(map(int, input().split()))

if n == 2:
    print(arr[1] - arr[0])
elif n == 3:
    print(arr[2] - arr[0])
else:
    dp = [
        arr[1] - arr[0],
        arr[2] - arr[0]
    ]
    for i in range(3, n):
        dp.append(min(
            arr[i] - arr[i-1] + dp[-2],
            arr[i] - arr[i-1] + dp[-1]
        ))
    print(dp[-1])