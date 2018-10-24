import mymodule #from mymodule import hap

def main():
    print('usemodule...',__name__)
    rst = mymodule.hap(10,20)
    print(rst)

if __name__ == '__main__':
    main()
