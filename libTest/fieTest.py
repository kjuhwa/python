# write mode 기존에 파일이 있으면 삭제하고 새로 기록

def fileWrite1():
    fp = open('test.txt', 'w') # w r a t b
    print(fp.tell())
    fp.write('abcdefghijkl')
    print(fp.tell())
    fp.write('hello')
    fp.close()

def fileRead1():
    fp = open('test.txt', 'r')
    rd = fp.read()
    fp.close()
    print(rd)

def fileWrite2():
    fp = open('test.txt', 'w') # w r a t b
    fp.write('abcdefghijkl')
    fp.write('hello')
    fp.close()

def fileRead2():
    fp = open('test.txt', 'r')
    while True:
        rd = fp.read(3)
        if not rd:
            break;
        print(rd)
    fp.close()

def fileWrite():
    fp = open('test.txt', 'w') # w r a t b
    fp.write('abc\ndef\nghi\njkl')
    fp.close()

def fileRead():
    fp = open('test.txt', 'r')
    rd = fp.readlines()
    print(rd)
    rd = [n.strip() for n in rd]
    print(rd)
    # for rd in fp:
    #     print(rd)
    # rd = fp.readline()
    # print(rd)
    # rd = fp.readline()
    # print(rd)
    fp.close()

fileWrite()
fileRead()

