# n은 화폐 종류 개수, m은 화폐로 만들고자 하는 합
n, m = map(int, input().split())

# 줄마다 화폐 단위 입력받기
array = []
for i in range(n):
    array.append(int(input()))

# 다이나믹 프로그래밍 테이블 생성
d = [-1] * (m + 1)

d[0] = 0

for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != -1:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == -1:
    print(-1)
else:
    print(d[m])

print(d)

### 틀린 이유.. DP 테이블 비교할 때, 최솟값을 구하는 것이므로
### DP 리스트를 초기화할 때, -1을 넣으면 안됨 -> 최솟값 구할때는 max(임의)값으로..