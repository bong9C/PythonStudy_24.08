# Chapter02_01
# 파이썬 완전 기초
# print 사용법


print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print()

# separator 옵션
print('P','Y','T','H','O','N',sep='|')
print('010','1234','5678',sep='-')
print('python','google.com',sep='@')

print()

# end 옵션

print('Welcome to', end='  ')
print('IT News', end='  ')
print('Web Site')

print()

# file 옵션

import sys

print('Learn Python', file=sys.stdout)
print()

# format 사용(d : 3, s : 'Python', f : 3.14...)
print('%s %s' % ('one','two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

print()

# %s
print('%10s' % ('nice')) # 앞에 인덱스에 마지막부터 문자가 채워짐
print('{:>10}'.format('nice~~'))

print('%10s' % ('nice'))
print('{:10}',format('nice')) # 반대 

print('{:$>10}'.format('nice')) # 빈 공간에 입력한 기호를 채워줌
print('{:^10}'.format('nice')) # 중앙 정렬

print('%.5s' % ('nice')) # 적인 숫자의 인덱스까지 잘림
print('%.5s' % ('Pythonstudy')) 
print('{:10.5}'.format('Pythonstudy')) # 열개의 자리중에 다섯자리만 붙여서 사용할 수 있다. 

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

# %f

print('%f' % (3.1497987897987))
print('{:f}'.format(3,564654646))
print('%06.2f' % (3.1498803798279)) # 여섯자리 중에 정수를 나타내고 소수점은 2까지 나타낸다. 
print('{:06.2f}'.format(3.1498803798279))

