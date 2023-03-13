# 이 문제를 처음 풀었을 때와 알고리즘은 같음.
# 대신 문자를 포함하는 집합에 대해, 비트마스킹 기법을 통해 처리함

from itertools import combinations

# 단어의 개수 n, 가르치는 글자 수 k
n, k = map(int, input().split())

# 각 단어에서, 글자에 대한 집합을 비트마스킹 처리해서 저장
word_list = []

for _ in range(n):
    s = input()
    temp = 0
    # 각 글자마다 비트마스킹 적용
    for x in s:
        temp |= (1 << (ord(x) - ord('a')))
    word_list.append(temp)

# 기본적으로 아는 글자리스트
default_list = ['a', 'n', 't', 'i', 'c']

# 추가적으로 가르쳐야하는 글자 리스트
optional_list = [chr(x) for x in range(ord('a'), ord('z')+1) if chr(x) not in default_list]

# default 글자를 배우지 못하는 경우, 가능한 단어는 0
if k < 5:
    print(0)
    exit()

answer = 0
# 기본 글자를 제외한 k-5만큼 추가적으로 글자를 뽑는 조합을 모두 고려
for combi in combinations(optional_list, k-5):
    # 각 조합마다 글자 집합을 비트마스킹
    each = 0
    count = 0
    # 기본 글자 비트마스킹
    for i in default_list:
        each |= (1 << (ord(i)-ord('a')))
    # 선택한 글자(조합의 글자) 비트마스킹
    for i in combi:
        each |= (1 << (ord(i)-ord('a')))
    
    # 각 단어와 글자조합을 비교
    for word in word_list:
        if word & each == word: # each 집합 안에 word가 있으면 가능
            count += 1

    answer = max(answer, count)

print(answer)