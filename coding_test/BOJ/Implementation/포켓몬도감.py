# https://www.acmicpc.net/problem/1620 s4
# 리스트로하니까 시간 초과 + index 에러남
# 딕셔너리 -> value -> key 찾기 방법 2가지
# 1. 그냥 반대 딕셔너리 만든다 // 2. for문으로 if문으로 체크(시간걸림)
# 1번 방법이 좀 더 코테에서는 유용한 듯

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    data = input().rstrip()
    dict[i] = data
    dict[data] = i

# 맞춰야하는 문제
for _ in range(m):
    data = input().rstrip()
    if data.isdigit():  # 숫자인 경우
        print(dict[int(data)])
    else:
        print(dict[data])

        
