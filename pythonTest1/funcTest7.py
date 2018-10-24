# for n in range(1,11):
#     if 10%n==0:
#         print(n)

def yaksu( num ):
    y =[]
    for n in range(1,num+1):
        if num%n==0:
            y.append(n)
    return y

rst = yaksu(10)
print(rst)
