exp = input().split('-')

answer = sum(map(int, exp[0].split('+'))) # -없으면 이 값이 정답으로 출력됨

for i in range(1, len(exp)):
    data = list(map(int, exp[i].split('+')))
    answer -= sum(data)

print(answer)