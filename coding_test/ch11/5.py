n, m = map(int, input().split())

balls = list(map(int, input().split()))

balls.sort()

result = n * (n-1) // 2
count = 1

for i in range(len(balls) - 1):
    if balls[i + 1] == balls[i]:
        count += 1
        continue
    if count != 1:
        result -= count * (count-1) // 2
        count = 1

if count != 1:
    result -= count * (count-1) // 2

print(result)