# permutations로 풀기
from itertools import permutations

# 수의 개수 n
n = int(input())

# 주어진 순열
num_data = list(map(int, input().split()))

# 각각 덧셈, 뺄셈, 곱셈, 나눗셈의 개수
op_data = list(map(int, input().split()))
op_list = ['+', '-', '*', '/']
op = []

for i in range(4): # 연산마다 각각
    for j in range(op_data[i]): # 각 연산의 개수만큼
        op.append(op_list[i])

# 가능한 모든 순열
op_candidates = permutations(op, n - 1)

max_val = -1e9
min_val = 1e9

for candidate in op_candidates:
    total = num_data[0]
    for i in range(1, n):
        if candidate[i - 1] == '+':
            total += num_data[i]
        elif candidate[i - 1] == '-':
            total -= num_data[i]
        elif candidate[i - 1] == '*':
            total *= num_data[i]
        elif candidate[i - 1] == '/':
            total = int(total / num_data[i])
    
    max_val = max(max_val, total)
    min_val = min(min_val, total)

print(max_val)
print(min_val)
