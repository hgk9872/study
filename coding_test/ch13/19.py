# 연산자 끼워넣기 p349
# 백트래킹 방법
# 백트래킹 강의 + N과 M 문제풀어보기

# 수의 개수 n
n = int(input())

# 주어진 순열
data = list(map(int, input().split()))

# 각각 덧셈, 뺄셈, 곱셈, 나눗셈의 개수
add, sub, mult, div = map(int, input().split())

max_val = 1e9
min_val = -1e9

def dfs(i, result):
    global max_val, min_val, add, sub, mult, div
    if i == n:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, result + data[i])