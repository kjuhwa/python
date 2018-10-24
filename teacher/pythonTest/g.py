s='abcdefghi'
#인덱스
# 0, 1,2,3,5,6, 7, 8
#            -3 -2  -1
#s[0] ='A'#immutable X
print( s[0] )
print( s[-1] )
#슬라이싱
#[시작인덱스:끝인덱스:증가치]
# 시작인덱스<= idx <끝인덱스
#shift+f10
print(s[1:4:1]) #1,2,3
print(s[1:4:2]) #1,3
print(s[:5:1])#0,1,2,3,4
print(s[:5])
print(s[1:]) #1 끝까지
print(s[::])
print(s[:])
print(s[-1:-5:-1])#-1,-2,-3,-4

