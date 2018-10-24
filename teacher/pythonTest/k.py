s ={10,20,30,40,50,20,20}
s.add(60)
s.add(70)
s.remove(30)
print( s )
print( type(s))
# print( s[0] )#index 사용 않됨
# 중복데이터허용 X
# 집합연산
s1={10,20,30}
s2={20,30,40,50}
print( s1 & s2) #교집합
print( s1 | s2) #합집합
print( s1 - s2) #차집합
