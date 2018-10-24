import random
def game():
    comData = [n for n in range(1,46)]
    c6 = random.sample(comData,6)
    meData = input('숫자6개 중복되지않게입력:')
    me = meData.split()
    me = [int(n) for n in me]
    print( me )
    print( c6)
    match = [ n for n in me if n in c6]
    print(match, len(match),'개 맞음')

def main():
    menu={1:game, 2:exit}
    while True:
        print('로또')
        print('='*20)
        print('1.게임시작','2.종료',sep='\n')
        nSel = int(input('메뉴를선택:'))
        menu[nSel]()
if __name__ == '__main__':
    main()
