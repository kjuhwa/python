def fn1():
    print('fn1 call')

def fn2():
    print('fn2 call')

def defaultFn():
    print('기타')

menu = {1:fn1, 2:fn2}
menu[1]()

menu.get(2, defaultFn)()
