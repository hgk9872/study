# 명령어 python3 tabto4.py a.txt b.txt

import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src) # 디폴트 'r' : 읽기모드
data = f.read()
f.close()

replaced_data = data.replace('\t', ' '*4)

f = open(dst, 'w')
f.write(replaced_data)
f.close()