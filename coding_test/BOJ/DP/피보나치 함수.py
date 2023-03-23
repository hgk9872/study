T = int(input())

for t in range(T):
    n = int(input())

    if n == 0:
        print("1 0")
    elif n == 1:
        print("0 1")
    else:
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][0] = 1
        dp[1][1] = 1
