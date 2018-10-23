s = '  abc  '
# 좌우 화이트스페이스(공백,\n,\t) 제거
print(s.strip())
s1 = '###abc###'
print(s1.strip('#'))
s2 = 'abc def ghi'
# 화이트스페이스기준으로 자른다
print(s2.split())
s3 = "000-1111-2222"
print(s3.split("-"))
s4 = 'i like python like program'
print(s4.replace('like', 'love'))
