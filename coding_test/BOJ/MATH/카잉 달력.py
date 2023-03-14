# 백준 6064 - 실버 1
# https://www.acmicpc.net/problem/6064
# 최소공배수 쓰니까 시간이 더 걸림,.

def fun(m, n, x, y):
    while x <= m * n:
				# 첫 x값에 +m을 계속 더하는 방식으로 나머지를 고정시키고,
				# 마지막 날짜까지 +m을 하면서 그 값의 나머지가
        if x%n == y%n:
            return x
        x += m
		# 끝까지 수행했을 때, 안나오면 -1 리턴
    return -1

num = int(input())
for _ in range(num):
    m, n, x, y = map(int, input().split())
    print(fun(m, n, x, y))