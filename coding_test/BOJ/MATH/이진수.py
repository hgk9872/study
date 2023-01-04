# BOJ 3460 - 이진수 (브론즈3)
# 수학

# 테스트 케이스의 개수 T
T = int(input())

# 개수만큼 반복
for _ in range(T):
    # 매 테스트마다 주어지는 양의 정수 n
    n = int(input())

    # 비트의 위치
    pos = 0

    while n > 0:
        # 만약 n의 자연수가 1이면 현재 비트의 위치 출력
        if n % 2 == 1:
            print(pos, end=' ')
        n //= 2
        pos += 1