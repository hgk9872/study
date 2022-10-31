# 정수 X를 입력받기
x = int(input())

# 최솟값 저장하는 리스트
d = [0] * 30001

for i in range(2, x + 1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1) # 현재 저장되어있는 값과 2로 나누었을 때의 값의 최솟값 비교    
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1) 
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
