n = int(input())
array = [0] * 1000001

x = list(map(int, input().split()))

for i in x:
    array[i] = 1

m = int(input())
need = list(map(int, input().split()))

for i in need:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')