# BOJ 2501 - 약수구하기 (브론즈3)
# 수학

# n의 약수들 중 k번째로 작은 수
n, k = map(int, input().split())

# 약수 저장 리스트
arr = []

# 1부터 돌면서 n의 약수 체크하기
for i in range(1, n + 1):
    # 나머지가 0 이면 약수
    if n % i == 0:
        arr.append(i)

if k > len(arr):
    print('0')
else:
    print(arr[k - 1])