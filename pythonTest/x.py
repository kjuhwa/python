#range(시작값, 끝값, 증가치)
# 시작값 <= 리스트값 < 끝값

r = range(1,5,1) #1,2,3,4 리스트
print(list(r))
r = range(1,11)
print(list(r))
r = range(1,11,2)
print(list(r))
r = range(5)
print(list(r))
for n in range(1,6):
    print(n)

sum = 0
for n in range(1,11):
    sum += n
print(sum)

for n in range(5):
    if n==2:
        continue
    print(n)

else:
    print('else...') # 정상탈출시 실행
