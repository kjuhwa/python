# my = [ n for n in range(1,6)]
# my = [ n*10 for n in range(1,6)]
# my = [ n*10 for n in range(1,6) if n%2==0 ]
def yaksu(num):
    return [n for n in range(1,num+1) if num%n==0]

my = [n for n in range(1,11) if 10%n==0]
print(my)
#연봉 세금 3.3을 제한 실수령액을 구하시요
salary = [1000,2000,3000,4000,5000]
sil = [ n-(n*0.033) for n in salary]
print(sil)
