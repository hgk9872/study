# 식량창고의 개수 입력
n = int(input())

# 각 식량창고에 저장된 식량의 개수 k 입력
array = list(map(int, input().split()))

# 다이나믹 프로그래밍 테이블 생성
d = [0] * 100

# d[0], d[1]에 대한 값 셋팅
d[0] = array[0]
d[1] = max(d[0], array[1])

for i in range(2, n): # 세 번째 인덱스부터 시작
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])