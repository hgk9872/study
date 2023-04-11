# https://www.acmicpc.net/problem/1712 b2

a, b, c = map(int, input().split())
# 고정비용, 가변비용, #판매가

# 노트에 적어서 공식을 구해보면
# 개수 = a / (c-b) 여기에 +1 해주면 됨

if (c - b) <= 0:
    print(-1)
else:
    x = a // (c - b)
    print(x + 1)