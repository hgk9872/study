from itertools import combinations

# 카드의 개수 n, 최댓값 m
n, m = map(int, input().split())

max_sum = 0

card_list = list(map(int, input().split()))

for cards in combinations(card_list, 3):
    if sum(cards) > m:
        continue
    max_sum = max(max_sum, sum(cards))

print(max_sum)
