# 백준 13305 - 실버3
# https://www.acmicpc.net/problem/13305
# 그리디

# 도시의 개수
n = int(input())

# 다음 도시까지 길이
dist = list(map(int, input().split()))

# 각 도시에서의 기름 가격
price = list(map(int, input().split()))

# 현재 이동할 때 사용되는 기름 가격
now_price = price[0]

# 처음 도시에서 그 다음 도시까지 이동할 때 비용
answer = now_price * dist[0]

# 두 번째 도시부터 다음 도시로 이동할 때 어떤 기름을 쓸 것인지
for i in range(1, n-1):
    # 다음 도시로 갈 때, 이전 기름가격과 새로운 기름가격 중 비교하여 사용
    if now_price * dist[i] > price[i] * dist[i]:
        now_price = price[i]
    answer += now_price * dist[i]

print(answer)