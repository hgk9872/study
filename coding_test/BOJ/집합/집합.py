# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다. 

# 연산의 수 m

import sys

input = sys.stdin.readline

m = int(input())

s = set()

for i in range(m):
    data = input().split()
    if data[0] == 'all':
        s = set([x for x in range(1, 21)])
    elif data[0] == 'empty':
        s = set()
    else:
        oper, x = data[0], data[1]
        if data[0] == 'add':
            s.add(int(x))
        elif data[0] == 'remove':
            s.discard(int(x))
        elif data[0] == 'check':
            if int(x) in s:
                print(1)
            else:
                print(0)
        elif data[0] == 'toggle':
            if int(x) in s:
                s.discard(int(x))
            else:
                s.add(int(x))
