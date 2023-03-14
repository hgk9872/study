# gcd 최대공약수 -> 유클리드 호제법
# 두 자연수 a, b에 대해 a를 b로 나눈 나머지 r
# a와 b의 최대공약수는 b와 r의 최대 공약수와 같음
# 이를 나머지가 0이 나올 때까지 반복한다

def gcd(a, b):
    r = a % b

    # 나머지 값이 0이 나올 때까지 반복
    while r != 0:
        a, b = b, r
        r = a % b
    
    # 최종적으로 나눈 b가 최대공약수
    return b

a, b = 10, 12
print('최대공약수 :', gcd(a, b))
print('최소공배수 :', a * b // gcd(a, b))