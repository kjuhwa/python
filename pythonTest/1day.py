#1
# 키 = int(input('키 : '))
# 몸무게 = int(input('몸무게 : '))
# 표준체중 = (키-100)*0.85
# 비만도 = 몸무게 / 표준체중 * 100
# if 비만도 <= 90 :
#     print('저체중')
# elif 90<비만도<110:
#     print('정상')
# elif 110<비만도<120:
#     print('과체중')
# else:
#     print('비만')

# 2-1
# m = int(input('m : '))
# mile = m * 0.000621
# print(m, ' m은 ', mile , ' 마일')

# 2-2
# 화씨 = int(input('화씨 : '))
# 섭씨 = 화씨 * -17.222222
# print(화씨, ' 화씨는 ', 섭씨 , ' 섭씨')

# 3-1
# 반지름 = int(input('반지름 : '))
# 높이 = int(input('높이 : '))
# 부피 = 3.14*반지름**2*높이
# print('원통의 부피는 ', 부피)

# 3-2
# 반지름 = int(input('반지름 : '))
# 높이 = int(input('높이 : '))
# 부피 = 1/3*3.14*반지름**2*높이
# print('원뿔의 부피는 ', 부피)

# 가로 = int(input('가로 : '))
# 세로 = int(input('세로 : '))
# 높이 = int(input('높이 : '))
# 부피 = 가로*세로*높이
# print('사각기둥의 부피는 ', 부피)

# 정수x = int(input('정수 : ')).__abs__()
# 정수y = int(input('정수 : ')).__abs__()
# 합 = 정수x + 정수y
# print(합)

# 정수x = int(input('정수 : '))
# 정수y = int(input('정수 : '))
# 정수z = int(input('정수 : '))
# print(max([정수x,정수y,정수z]))

년도 = int(input('년도 : '))
if (년도%4==0 and 년도%100!=0) or 년도%400==0:
    print('윤년')
else:
    print('윤년X')
나이 = 0 if 2018-년도+1<0 else 2018-년도+1
print('나이 : ', 나이)
띠 = 나이 % 12
print('띠 : ', 띠)
