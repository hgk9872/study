
dict = {'a' : 1, 'b': 2}

if 1 in dict:
    print('잇어요')
else:
    print('없어요')

if 'a' in dict:
    print('잇어요')
else:
    print('없어요')

    # => 해시값을 찾을 때 ... 키값으로 찾는다.

if 'a' in dict.keys():
    print('잇어요')
else:
    print('없어요')

    # 이렇게도 된다.
    # 즉, 보기에 직관적인 keys() 에 있는지 확인할 수도 있고 (권장)
    # 그냥 바로 키값이 있는지 ..도확인할 수 있다