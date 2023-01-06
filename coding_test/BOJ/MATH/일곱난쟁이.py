# BOJ 2309 - 일곱 난쟁이 (브론즈1)
# 정렬

### combinations 사용코드
from itertools import combinations

arr = [int(input()) for _ in range(9)]

# combinations으로 나오는 조합에 대한 각 객체는 tuple타입
for members in combinations(arr, 7):
    if sum(members) == 100:
        for member in sorted(members):
            print(member)
        break