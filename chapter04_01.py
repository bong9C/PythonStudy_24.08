# Chapter04_01
# 파이썬 제어문
# IF 실습

# 기본 형식 
print(type(True)) # 0이 아닌 수, "abc", [1,2,3...], (1,2,3...)
print(type(False)) # 0, "", [], (), {}...

# 예1

if True:
    print('Good')

if False:
    print('Bad')

# 예2
if False:
    print('Bad!')
else:
    print('Good!')

# 관계 연산자 
# >, >=, <, <=, ==, !=
x = 15
x = 10

# 양변이 같은 경우 거짓 
print(x == y)

# 양 변이 다를 때 참 
print(x != y)

# 왼쪽이 클 때 참
print(x > y)

# 왼쪽이 크거나 같을 때 참 
print(x >= y)

# 오른쪽이 클 때 참 
print(x < y)

# 오른쪽이 크거나 같을 때 참 
print(x <= y)

city = ""
if city:
    print("You are in:",city)
else:
    print("plz enter your city")

city = "Seoul"
if city:
    print("You are in:",city)
else:
    print("plz enter your city")