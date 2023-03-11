# 6603
# https://www.acmicpc.net/problem/6603

# 라이브러리를 사용하는 경우 풀이가 간단하지만,
# 재귀, 브루트포스 연습을 위해 라이브러리 사용하지 않고 풀이

def dfs(cnt, start):
    if cnt == 6:
        print(*temp)
        return

    for i in range(start, len(arr)):
        temp.append(arr[i])
        dfs(cnt+1, i+1)
        temp.pop()


while True:
    data = list(map(int, input().split()))

    if data[0] == 0:
        break

    arr = data[1:]

    temp = []
    dfs(0, 0)
    print()