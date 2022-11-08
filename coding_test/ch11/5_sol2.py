# 답안지를 보고 괜찮다고 생각한 풀이
# 기수정렬을 사용한 풀이방법
# 볼링공 무게가 10까지만 존재할 수 있으므로(범위한정) 이 경우 기수정렬을 노리는 문제같음

n, m = map(int, input().split())

balls = list(map(int, input().split()))

# 기수정렬을 위한 리스트
array = [0] * 11

# 무게마다의 볼링공 개수 저장
for i in balls:
    array[i] += 1

# 볼링공 조합의 모든 경우의 수
result = n * (n-1) // 2

# 볼링공 최대 무게까지 반복하면서 같은 무게를 고르는 조합의 경우의 수를 뺌
for i in range(m + 1):
    if array[i] > 1:
        result -= array[i] * (array[i]-1) //2

print(result)