# 골드4
# https://www.acmicpc.net/problem/1062

from itertools import combinations

# 단어의 개수n, 가능한 글자의 개수 k
n, k = map(int, input().split())

origin = ['a', 'n', 't', 'i', 'c']
alpha = []

word_list = []
for _ in range(n):
    word = input()
    word_list.append(word)
    # 주어진 단어 중, origin에 포함된 글자가 아닌 경우 alpha 추가
    for c in word:
        if c not in origin:
            alpha.append(c)

alpha = set(alpha)

# 가르치는 글자가 5개 이하인 경우 어떤 글자도 만들 수 없음
if k <= 5:
    print(0)
    exit()

answer = 0
# alpha의 모든 조합 탐색하면서 최댓값 저장
for c in combinations(alpha, k-5):
    count = 0
    # 각 단어마다 검사
    for word in word_list:
        check = True
        # 단어의 각 문자마다 찾아서...
        for w in word:
            # 만들수 없는 경우
            if w not in c and w not in origin:
                check = False
                break
        # 해당 단어를 읽을 수 있다면 count 증가
        if check:
            count += 1
    answer = max(answer, count)

print(answer)
