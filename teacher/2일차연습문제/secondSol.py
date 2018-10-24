def obesity( height,weight):
    avg_weight=(height-100)*0.85
    val=weight/avg_weight*100
    if val <= 90:
        rst ='저체중'
    elif 90 < val <= 110:
        rst='정상'
    elif 110 < val <= 120:
        rst ='과체중'
    else:
        rst ='비만'
    return rst
def ttee( year ):
    return ('원숭이', '닭', '개', '돼지', '쥐',
            '소', '호랑이', '토끼', '용', '뱀',
            '말', '양')[year%12]

def maxMin( a,b,c):
    nmax = a if a>b else b
    nmax = nmax if nmax > c else c
    nmin = a if a<b else b
    nmin = nmin if nmin < c else c
    return nmax, nmin

def listHap( dt ):
    nsum=0
    for n in dt:
        nsum = nsum+n # nsum+=n
    return nsum
def listAvg( dt ):
    nsum=0
    for n in dt:
        nsum = nsum+n # nsum+=n
    return nsum/len(dt)

def gugudan():
    for n in range(2,10):
        for m in range(1,10):
            print( '%dX%d=%2d'%(n,m,n*m)  )
# data =[]
def inputData():
    data =[]
    while True:
        name = input("이름:")
        kor = int( input('국어:'))
        eng = int( input('영어:'))
        data.append( (name,kor,eng) )
        yn = input('계속입력(y/n):')
        if yn=='n':
            break
    return data

def outputData(data):
    for n,k,e in data:
        # print(n,k,e )
        print('이름:%s 국어:%d 영어:%d'%(n,k,e))

dt = inputData()
outputData(dt)

# data =[]
# while True:
#     name = input("이름:")
#     kor = int( input('국어:'))
#     eng = int( input('영어:'))
#     data.append( (name,kor,eng) )
#     yn = input('계속입력(y/n):')
#     if yn=='n':
#         break
#
# for n,k,e in data:
#     # print(n,k,e )
#     print('이름:%s 국어:%d 영어:%d'%(n,k,e))
#



# gugudan()
# data=[10,20,30,40]
# print( listAvg(data) )


# print( listHap(data) )
# print( maxMin(10,30,20) )
# print( ttee(2018) )
# o = obesity(170, 70)
# print(o)





