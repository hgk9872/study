# 이코테 교재 그리디 실전 2번

# n개의 자연수, 수가 더해지는 횟수 m, 최대 k번 더할 수 있다
n, m, k = map(int, input().split())

# 주어진 n개의 자연수 배열
arr = list(map(int, input().split()))
arr.sort()

first = arr[n-1] # 가장 큰 수
second = arr[n-2] # 그 다음으로 큰 수


result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    else:
        result += second
        m -= 1

print(result)