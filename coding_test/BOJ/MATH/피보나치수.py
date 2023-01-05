# BOJ 10870 - 피보나치수5 (브론즈2)
# 수학

# dp방식말고, 재귀로 가장 간단하게 구현
# n번째 피보나치 수 구하기
n = int(input())

def fibo(n):
    if n <= 1:
        return n
    # n >= 2부터 점화식 적용
    return fibo(n-1) + fibo(n-2)

print(fibo(n))