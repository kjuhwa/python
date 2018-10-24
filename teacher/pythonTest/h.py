s='  ab  c  '
s1='###abc###'
s2='abc def ghi'
s3='000-1111-2222'
s4='i like python like program'
#좌우 화이트스페이스(공백,\n,\t)제거
print( s.strip() )
print( s1.strip('#') )
#화이트스페이스기준으로 자른다
print(s2.split() )
print(s3.split('-'))

print( s4.replace('like','love'))
