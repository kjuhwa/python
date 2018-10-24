def 비만도(키, 몸무게):
    표준체중 = (키-100)*0.85
    비만도 = 몸무게 / 표준체중 * 100
    if 비만도 <= 90 :
        print('저체중')
    elif 90<비만도<110:
        print('정상')
    elif 110<비만도<120:
        print('과체중')
    else:
        print('비만')

# 키 = int(input('키 : '))
# 몸무게 = int(input('몸무게 : '))
# 비만도(키, 몸무게)

def 띠(년도):
    ttee = ('원숭이','닭','개','돼지','쥐','소','범','토끼','용','뱀','말','양')
    return ttee[ 년도%12 ]

# 년도 = int(input('년도 : '))
# print(띠(년도))

def 큰값and작은값(정수들):
    큰값 = max(정수들)
    작은값 = []
    for 값 in 정수들:
        if 값 != 큰값:
            작은값.append(값)
    return 큰값, 작은값

# 정수들 = []
# for n in range(3):
#     정수 = int(input('정수 : '))
#     정수들.append(정수)
#
# print(큰값and작은값(정수들))

def 합(인자):
    누적 = 0
    for 값 in 인자:
        누적 += 값
    return 누적

print(합([10,20,30,40]))
