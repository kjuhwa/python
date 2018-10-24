import random

my = [n for n in range(1,11)]
print(my)
# random.shuffle(my)
# print(my)

print(random.sample(my, 3))

# for n in range(5):
#     print(random.randint(1,10)) # 1~10까지 임의 숫자 반환
