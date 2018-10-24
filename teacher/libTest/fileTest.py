#write mode 기존에 파일이있으면 삭제하고 새로 기록
def fileWrite1():
    fp = open( 'test.txt','w') #w r a  t b
    print( fp.tell() )
    fp.write('korea')
    fp.seek(3) #기록대상위치 강제변경
    print( fp.tell() )
    fp.write('hello')
    fp.close()
def fileWrite2():
    fp = open( 'test.txt','w') #w r a  t b
    fp.write('abcdefghijkl')
    fp.close()
def fileRead1():
    fp = open( 'test.txt','r')
    while True:
        rd = fp.read(3)
        # if rd=='':
        if not rd:
            break
        print( rd )
    fp.close()
def fileWrite():
    fp = open( 'test.txt','w') #w r a  t b
    fp.write('abc\ndef\nghi\njkl')
    fp.close()
def fileRead():
    fp = open( 'test.txt','r')
    rd = fp.readlines()
    print(rd )
    rd = [n.strip() for n in rd]
    print(rd)
    # for rd in fp:
    #     print( rd )
    # rd = fp.readline()
    # print(rd)
    # rd = fp.readline()
    # print(rd)
    fp.close()
fileWrite()
fileRead()




