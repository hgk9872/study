# 럭키 스트레이트 (p321)

# 점수의 자릿수는 항상 짝수로 들어옴

score = input()

mid_idx = len(score) // 2

left = 0
right = 0

# 왼쪽 부분
for i in range(mid_idx):
    left += int(score[i])

# 오른쪽 부분
for j in range(mid_idx, len(score)):
    right += int(score[j])

if left == right:
    print("LUCKY")
else:
    print("READY")