
# 10진수 -> 2진수
Dlist = [10, 8, 1, 31]

for num in Dlist:
    blist = []
    # 몫이 0이 될 때 까지 반복
    while num != 0:
        blist.append(str(num % 2))
        num = num // 2
    # ''.join(reversed(blist))
    print(''.join(list(reversed(blist))))