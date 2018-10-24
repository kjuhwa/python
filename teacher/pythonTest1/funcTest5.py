import sys
#파이썬에 모든 변수는 참조변수(C언어포인터)

# list myList = new list();
myList = [10,20,30] #list([10,20,30])
print( sys.getrefcount(myList)-1 )
# myList1 = myList #shallow copy(주소만복사)
# myList1 = [10,20,30]
myList1 = myList.copy() #deep copy
myList1[0] = 100
print( sys.getrefcount(myList)-1 )
print( id(myList) )
print( id(myList1) )
print( myList is myList1 )
print(myList)
