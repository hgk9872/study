# 백준 1759 - 골드5
# 전형적인 dfs 브루트포스 문제
# 이렇게 조건이 주어지는 경우 dfs로 풀어야 적합함

# m은 모음, z는 자음 개수
def dfs(now, cnt, m, z):
    if cnt == l:
        if m >= 1 and z >= 2:
            print(''.join(temp))
        return

    for i in range(now, c):
        if data[i] not in temp:
            temp.append(data[i])
            # 모음, 자음 분류해서 count 증가
            if data[i] in m_list:
                dfs(i, cnt+1, m+1, z)
            else:
                dfs(i, cnt+1, m, z+1)
            temp.pop()


# 서로 다른 l개의 알파벳 소문자, 서로 다른 문자 종류의 개수 c
l, c = map(int, input().split())
data = sorted(list(input().split()))
temp = []
m_list = ['a', 'e', 'i', 'o', 'u']

dfs(0, 0, 0, 0)