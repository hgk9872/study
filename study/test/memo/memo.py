# python memo.py -a "Life is too short"
# 명령어를 입력했을 때 해당 내용이 메모에 추가되게..

import sys

# sys.argv[0]은 실행한 파일 이름(memo.py)
option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt', 'r')
    memo = f.read()
    f.close()
    print(memo)