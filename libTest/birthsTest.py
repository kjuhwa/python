


fp = open('births.txt', 'r')
# rd = fp.readlines()
# rd = [int(n.split(',')[1]) for n in rd]
# print(rd)
# print(sum(rd))

mList = []
for rd in fp:
    y,m,f = rd.split(',')
    mList.append(int(m))

print(mList)
print(sum(mList))
