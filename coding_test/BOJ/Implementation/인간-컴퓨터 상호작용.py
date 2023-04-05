# 백준 16139 - 실버1
# https://www.acmicpc.net/problem/16139
# 구현문제(?) 오히려 DP개념하고 가까운 듯..

word = list(input()) # 입력받은 단어
q = int(input()) # 질문의 수

arr = [[0] * 26 for _ in range(len(word))]

# 알파벳 26개 문자에 대해서, 미리 계산해놓는다 (시간초과 문제 해결을 위해)
# 문자열 첫 부분부터 갱신
for i in range(len(word)):
    if i == 0:
        arr[i][ord(word[i])-ord('a')] = 1
    else: # 두 번째 인덱스부터
        for j in range(26):
            arr[i][j] = arr[i-1][j] # 일단 직전 개수값 가져온다
        arr[i][ord(word[i])-ord('a')] += 1 # 현재 인덱스에 해당하는 문자만 증가

for k in range(q):
    c, l, r = list(input().split())
    l = int(l)
    r = int(r)
    if l == 0:
        answer = arr[r][ord(c)-ord('a')]
    else:
        answer = arr[r][ord(c)-ord('a')] - arr[l-1][ord(c)-ord('a')]
    print(answer)
