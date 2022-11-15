# 카드 정렬하기 p554
# https://www.acmicpc.net/problem/1715
# 시간초과 코드
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

card_list = []

for _ in range(n):
    card_list.append(int(input()))

# 먼저 오름차순으로 정렬
card_list.sort()

# 큐로 만드는데, 앞에서 부터 2개씩 뽑는다.
# 만약 꺼낸 두개의 합의 알맞은 위치를 찾아서 삽입
# 반복

q = deque(card_list)

# 총 비교횟수
sum = 0
while True:
    # 큐에 원소가 하나 남으면
    if len(q) == 1:
        result = q.popleft()
        break
    # 두 개를 뽑음
    card1 = q.popleft()
    card2 = q.popleft()
    sum = card1 + card2
    # 맨 앞에 삽입
    q.appendleft(sum)
    # 다음 인덱스부터 반복
    for i in range(len(q) - 1):
        # 만약 다음 인덱스보다 작으면 break
        if q[i] <= q[i + 1]:
            break
        else: # 다음인덱스보다 크면 두개위치를 스왑
            q[i], q[i + 1] = q[i + 1], q[i]

print(result)
