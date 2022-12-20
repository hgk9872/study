# BOJ 14225 - 부분수열의 합
def dfs(start, depth, size):
    if depth == size:
        idx = sum(case)
        result[idx] = 1
        return
    for i in range(start, len(data)):
        case[depth] = data[i]
        dfs(i + 1, depth + 1, size)

n = int(input())
data = list(map(int, input().split()))

max_val = sum(data)
result = [0] * (max_val + 2)

# 사이즈가 n인 수열의 조합
for i in range(1, n + 1):
    case = [0] * i
    dfs(0, 0, i)

# for i in range(1, max_val + 1):
#     if result[i] == 0:
#         print(i)
#         break

# if i == max_val:
#     print(max_val + 1)

print(result[1:].index(0) + 1)