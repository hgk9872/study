# 백준 2212 - 그리디
# https://www.acmicpc.net/problem/2212

n = int(input())
k = int(input())
arr = list(map(int, input().split()))
arr.sort()

dist_list = []

for i in range(len(arr) - 1):
    dist_list.append(arr[i+1] - arr[i])

# 가장 큰 값부터, k-1개 지운다
dist_list.sort(reverse=True)
print(sum(dist_list[k-1:]))