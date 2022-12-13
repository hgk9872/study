# BOJ 1182 - 부분수열의 합


def dfs(start, depth, size):
    global count
    if depth == size:
        if sum(result) == s:
            count += 1
        return
    for i in range(start, len(data)):
        result[depth] = data[i]
        dfs(i + 1, depth + 1, size)
        
n, s = map(int, input().split())
data = list(map(int, input().split()))

count = 0

# 각 dfs마다 뽑는 원소의 개수가 1~6인 부분수열의 합을 구한다
for i in range(1, n + 1):
    result = [0] * i
    dfs(0, 0, i)

print(count)