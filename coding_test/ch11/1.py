# 모험가 길드 문제 (p.311)
# 최대 모험가 그룹 개수
# 정렬 후, 가장 큰 수부터..
# 전체 수 구하고.
# 가장 큰 모험가부터 반복
# total 에서 빼감
# 만약 공포도가 < 남은 인원보다이면 종료

n = int(input())

# 전체 그룹의 모험가 입력받기, 내림차순 정렬
group = list(map(int, input().split()))
group.sort(reverse=True)

total = len(group)
count = 0

for i in range(len(group)):
    part = group[i]
    total -= part
    if total < 0:
        break
    count += 1

print(count)

