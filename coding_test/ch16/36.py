# 편집 거리 p382

str1 = input()
str2 = input()

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            