# https://www.acmicpc.net/problem/1181 실5

# 길이가 짧은 것부터,
# 길이가 같으면 사전 순으로

# 실제로 풀 때에는 사전 순으로 정렬 후, 그 다음 길이순
n = int(input())

arr = [input() for _ in range(n)]
arr = list(set(arr))

arr.sort() # 사전 순 정렬
arr.sort(key = lambda x:len(x))

for i in range(len(arr)):
    print(arr[i])