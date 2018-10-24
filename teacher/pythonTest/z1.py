data=[] #list()
for n in range(2):
    product = input('제품명:')
    cnt = int(input('수량:'))
    # data.append( (product,cnt) )
    data.append( {'product':product,'cnt':cnt})
print(data)
print('='*20)
print('제품명  수량')
print('='*20)
for d in data:
    print(f'{d["product"]}  {d["cnt"]}')
    # print('%(product)s  %(cnt)d'%d )
# for p,c in data:
#     print('%s   %d'%(p,c))
# for t in data:
#     print('%s   %d'%t)
