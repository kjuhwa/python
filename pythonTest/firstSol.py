#1번
height=int(input('신장(cm):'))
weight=int(input('몸무게(kg):'))

std_weight=(height-100)*0.85
obesity=weight/std_weight*100
if obesity <= 90:
    print('저체중')
elif 90 < obesity <= 110:
    print('정상')
elif 110 < obesity <= 120:
    print('과체중')
else:
    print('비만')
print('\n\n')

#2번
input_m=int(input("미터:"))
print("마일:", input_m*0.000621 )

F=int(input("temperature:"))
print("섭씨",  (F-32) * 5/9 )

#3번
r=int(input('radius:'))
height=int(input('height:'))
print("원기둥의부피:", r**2*3.14*height )
print("원뿔의부피:", r**2*3.14*height/3 )
가로=int(input('가로:'))
세로=int(input('세로:'))
높이=int(input('높이:'))
print('사각기둥의부피:',가로*세로*높이)

num1 = int(input('정수1:'))
num2 = int(input('정수2:'))
num1 = -1*num1 if num1<0 else num1
num2 = -num2 if num2<0 else num2
print('절대값의합:', num1+num2 )

num1 = int(input('정수1:'))
num2 = int(input('정수2:'))
num3 = int(input('정수3:'))
mx = num1 if num1>num2 else num2
mx = mx if mx > num3 else num3
print("가장큰값:",mx)

year = int(input('연도:'))
y= '윤년' if year%4==0 and year%100 !=0 or year%400==0 else '윤년아님'
print(y)
#5.
nai = 2018-year +1
print( '나이:', nai )

ttee = ('원숭이','닭','개','돼지','쥐','소','범','토끼','용','뱀','말','양')
print('띠:', ttee[ year%12 ] )
#6.
product = int(input('상품가격:'))
pay = int(input('지불액:'))
change = product-pay
c500 = change//500
change = change%500
c100 = change//100
change = change%100
c50 = change//50
change = change%50
c10 = change//10
print("500원",c500,'100원', c100,'50원',c50, '10원', c10)



