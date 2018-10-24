import sys
#제너레이터는 연산된 결과 전체를 메모리로 잡지 않는다
#next내장함수에 의해 연산한다
myGen = ( n*10 for n in range(1,6)) #tuple(X)
print( list(myGen)) #[ next(myGen),next(myGen),..]

# for n in myGen: #next(myGen) ... stopiteration예외발생
#     print(n)

# print( next(myGen) )
# print( next(myGen) )
# print( next(myGen) )
# print( next(myGen) )
# print( next(myGen) )
# print( next(myGen) ) #stop iteration 예외발생

# myList = [n for n in range(1,1000)]
#
# print( myGen, sys.getsizeof(myGen) )
# print( sys.getsizeof(myList))
# print( myList)
