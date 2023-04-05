n = int(input())
k = int(input())

def binary_search(target, start, end):
    while(start <= end):
        mid = (start + end) // 2

        cnt = 0
        for i in range(1, n+1):
            cnt += min(mid//i, n)

        if cnt >= target: # 이 코드는 중복값이 있을 때, 정답에 해당하는 가장 왼쪽 값을 리턴한다
            end = mid-1
        else:
            start = mid+1
    return start


print(binary_search(k,1,n*n))
# 주석 뜻 : 즉, 3 7 을 입력했을 때와, 3 8을 입력했을 때 나오는 index값은 동일함
# 따라서 