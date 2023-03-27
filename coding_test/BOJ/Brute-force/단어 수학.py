# 백준 1339 - 골드4
# https://www.acmicpc.net/problem/1339
# 그리디 푸는 법 정확히 몰라서 다른사람 코드보고 품
# 중복되는 값에 대해서 처리하는 방법을 생각했는데, 그 부분을 처리 안해도 코드가 돌아감
# 이 경우 1번 예시인 AAA, AAA가 222 로 저장이 되는데, 바로 9를 곱해주면 결괏값이 나옴
# 생각해보면 AAA, AAA -> (111 * 9 + 111 * 9)이므로 이는 (222)*9와 같음

n = int(input())

words = [list(input()) for _ in range(n)]
alpha_dict = {}

for word in words:
    # 단어의 각 문자마다 정보 갱신해서 딕셔너리에 저장
    for i in range(len(word)):
        if word[i] not in alpha_dict:
            alpha_dict[word[i]] = 10 ** (len(word) - i - 1)
        else: # 이미 딕셔너리에 등록된 알파벳이라면
            alpha_dict[word[i]] += 10 ** (len(word) - i - 1)

# value기준으로 내림차순 정렬 후 리스트로 변환
alpha_list = sorted(alpha_dict.items(), key=lambda x: -x[1])

num = 9  # 가장 큰 수인 9부터 할당
answer = 0
for char, value in alpha_list:
    # print(char, value)
    answer += value * num
    num -= 1

print(answer)