# https://www.acmicpc.net/problem/9996 - s3

n = int(input())
p1, p2 = input().split('*')

for _ in range(n):
    word = input()
    # 만약 길이조건에 어긋난다면 NO 출력
    if len(p1 + p2) > len(word):
        print('NE')
        continue
    
    # 앞 뒤 패턴이 일치하는지 확인
    if word[:len(p1)] == p1 and word[-len(p2):] == p2:
        print('DA')
    else:
        print('NE')
