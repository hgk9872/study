

n = int(input())

arr = [input().split() for _ in range(n)]

arr.sort(key = lambda x:int(x[0]))

for i in range(n):
    print(arr[i][0], arr[i][1])