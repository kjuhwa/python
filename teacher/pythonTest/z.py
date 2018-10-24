#이름, 국어,영어
data1 =[('홍길동',90,60),('이순신',70,80),('임꺽정',50,80)]
data2 =[{'name':'홍길동','kor':90,'eng':60},
        {'name':'이순신','kor':70,'eng':80},
        {'name':'임꺽정','kor':50,'eng':80}]
for d in data2:
    # print(d)
    print("이름:%(name)s 국어:%(kor)d 영어:%(eng)d"%d )

# for d in data1:
#     print(d)
# for n,k,e in data1:
#     # print(n,k,e)
#     # print('이름:%s 국어:%d 영어:%d'%(n,k,e) )
#     print( f'이름:{n} 국어:{k} 영어:{e}')
