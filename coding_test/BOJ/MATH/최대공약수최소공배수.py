# BOJ 2609 - 최대공약수와 최소공배수(브론즈1)
# 수학
# 유클리드 호제법 사용해야함..

#### 틀린 풀이
# # 주어진 자연수 두 개
# a, b = map(int, input().split())
# min_value = min(a, b)
# max_value = max(a, b)

# # 최대공약수 출력
# for i in range(min_value, 0, -1):
#     if a % i == 0 and b % i == 0:
#         print(i)
#         break

# while True:
#     if max_value % a == 0 and max_value % b == 0:
#         print(max_value)
#         break
#     max_value += 1
