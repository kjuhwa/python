# 이름, 국어, 영어
data1 = [('홍길동',90,60),('이순신',70,80),('임꺽정',50,80)]
data2 = [{'name':'홍길동','kor':90,'eng':60},
         {'name':'이순신','kor':70,'eng':80},
         {'name':'임꺽정','kor':50,'eng':80}]
# for d in data1:
#     print(d)
# for n,k,e in data1:
#     print(n,k,e)
#     print('이름:%s 국어:%d 영어:%d'%(n,k,e))
#     print(f'이름:{n} 국어:{k} 영어:{e}')
# for d in data2:
#     print(d)
#     print('이름:%(name)s 국어:%(kor)d 영어:%(eng)d'%d)

# data3 = [{'제품명':'xxxx','수량':5},{'제품명':'xxxx','수량':5}]
# print('----------------------------------')
# print('%10s %10s'%('제품명','수량'))
# print('----------------------------------')
# for d in data3:
#     print('%(제품명)13s %(수량)10d'%d)

data = []
for n in range(2):
    product = input('제품명 : ')
    cnt = int(input('수량 : '))
    data.append((product,cnt))
print(data)
print('='*30)
print('제품명   수량')
print('='*30)
for p,c in data:
    print('%s     %d'%(p,c))
