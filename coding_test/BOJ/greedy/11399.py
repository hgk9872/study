# BOJ 11399 ATM - 실버4

# 사람의 수 n
n = int(input())

# 각 사람이 돈을 인출하는데 필요한 시간 리스트
arr = list(map(int, input().split()))
arr.sort()

result = 0

# 각 사람들이 걸리는 시간
for i in range(n):
    time = sum(arr[:i+1])
    result += time

print(result)