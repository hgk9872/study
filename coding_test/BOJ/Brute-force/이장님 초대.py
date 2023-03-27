# 백준 9237 - 실버5
# 그리디

n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

answer = 0

for i in range(n):
    arr[i] += i + 1 # 묘목을 구입한 날이 1일 이므로 하루씩 더 추가

print(max(arr) + 1) # 다 심은 다음날 초대해야 하므로 +1