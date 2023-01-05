# BOJ 2460 - 지능형 기차2 (브론즈3)
# 수학, 구현

# 현재 기차에 탑승한 인원
train = 0
max_val = train
# 1번역부터 10번역까지 정차
for _ in range(10):
    data_out, data_int = map(int, input().split())
    # 탈때마다 승객 수 바뀜
    flow = data_int - data_out
    train += flow
    # 기차 인원수 최댓값 갱신
    if train >= max_val:
        max_val = train

print(max_val)