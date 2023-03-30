# 백준 1449 - 실버3, 그리디
# https://www.acmicpc.net/problem/1449

# 물이 새는 곳의 개수 n, 테이프 길이 l
n, l = map(int, input().split())

data = sorted(list(map(int, input().split())))

# 테이프의 길이가 2일 때, 만약 첫 번째 구멍 위치가 1이라면
# 1부터 +2-1 -> 2 : 구멍 위치가 2인 경우까지 커버 가능
start = data[0]
count = 1

for i in range(1, len(data)):
    # 테이프 길이가 모자라면 새 테이프를 붙인다
    if data[i] > start + l - 1: 
        count += 1
        start = data[i]

print(count)
        