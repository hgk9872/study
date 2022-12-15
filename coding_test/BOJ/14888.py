# BOJ 14888 - 연산자 끼워넣기

# 수의 개수 n
n = int(input())

# 주어진 수열
seq = list(map(int, input().split()))

# 각 연산자의 개수 +, -, *, //
oper_num = list(map(int, input().split()))

max_val = -1e9
min_val = 1e9


def dfs(idx, total):
    global max_val, min_val
    # 종료조건 : 연산의 개수가 n번까지 될 때까지
    if idx == n:
        max_val = max(max_val, total)
        min_val = min(min_val, total)
        return
    # 각 연산마다..
    for i in range(4):
        if oper_num[i] > 0:
            oper_num[i] -= 1
            if i == 0:
                dfs(idx + 1, total + seq[idx])
            elif i == 1:
                dfs(idx + 1, total - seq[idx])
            elif i == 2:
                dfs(idx + 1, total * seq[idx])
            else:
                dfs(idx + 1, int(total / seq[idx]))
            oper_num[i] += 1


# 1부터 시작
dfs(1, seq[0])

print(max_val)
print(min_val)