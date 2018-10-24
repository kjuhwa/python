import random

def 결과(user, com):
    rst = []
    for n in com:
        for u in user:
            if n == int(u):
                rst.append(n)
    return rst

while True:
    user = input('숫자 6개 중복되지 않게 입력 : ').split(' ')
    com = [random.randint(1,45) for n in range(6)]
    print('컴퓨터랜덤: ',com)
    rst = 결과(user, com)
    print('결과: ',rst)
    con = input('계속하시겠습니까(y/n) : ')
    if con == 'n':
        break;
