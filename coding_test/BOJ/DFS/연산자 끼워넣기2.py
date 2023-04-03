# 백준 15658 - 실버2
# https://www.acmicpc.net/problem/15658

def dfs(idx, now):
    global max_answer, min_answer
    if idx == n - 1:
        max_answer = max(max_answer, now)
        min_answer = min(min_answer, now)
        return

    # 각 연산자로 계산
    for i in range(4):
        if arr[i] > 0: # 계산할 연산자 개수가 남아있는 경우에만
            if i == 0:  # 덧셈
                arr[i] -= 1
                dfs(idx + 1, now + data[idx + 1])
                arr[i] += 1
            elif i == 1:
                arr[i] -= 1
                dfs(idx + 1, now - data[idx + 1])
                arr[i] += 1
            elif i == 2:
                arr[i] -= 1
                dfs(idx + 1, now * data[idx + 1])
                arr[i] += 1
            else: # 나눗셈
                arr[i] -= 1
                if now >= 0:
                    dfs(idx + 1, now // data[idx + 1])
                else:
                    dfs(idx + 1, -(-now // data[idx + 1]))
                arr[i] += 1


n = int(input()) # 수의 개수
data = list(map(int, input().split()))
# 차례대로 +, -, *, %의 개수
arr = list(map(int, input().split()))

min_answer = 1e9
max_answer = -1e9

dfs(0, data[0]) # 0번 인덱스부터 시작
print(max_answer, min_answer)