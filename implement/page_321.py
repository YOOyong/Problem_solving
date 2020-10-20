#str을 단어단위로 쪼갤떄는 그냥 list() 하면 됨. split()은 기본 블랭크 단위임.

num = str(input())
a = list(map(int, list(num[:(len(num)//2)])))
b = list(map(int, list(num[(len(num)//2):])))
if sum(a) == sum(b):
    print('LUCKY')
else:
    print('READY')


