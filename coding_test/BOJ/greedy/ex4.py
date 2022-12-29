# 이코테 교재 그리디 실전 4번

# n - 1, n // k 두 가지 연산만 가능
n, k = map(int, input().split())

count = 0

while True:
    if n == 1:
        break
    if n % k == 0:
        n = n // k
    else:
        n -= 1
    count += 1

print(count)