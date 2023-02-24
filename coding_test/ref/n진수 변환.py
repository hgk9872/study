

# 들어오는 숫자 num을 n진수 문자열로 바꾸기
def change(num, n):
    N = '0123456789ABCDEF'
    result = ''

    if num == 0:
        return '0'

    while num > 0: # 이진수 변환을 생각해보면 num % 2
        result += N[num % n]
        num = num // n
    
    return result[::-1]

print(change(8, 2))
