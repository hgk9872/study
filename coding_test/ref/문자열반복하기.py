origin = 'abcd'  # 기존 문자열
num = 10    # 최종 문자열의 길이

repeated_str = origin * (num // len(origin)) + origin[:num % len(origin)]
# 기존 문자열을 2번만큼 반복하고, 나머지 수만큼 더해준다
print(repeated_str)