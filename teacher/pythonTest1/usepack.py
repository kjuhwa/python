import mymath.circle as c
# import mymath.calc
from mymath.calc import cmToInch
# rst = mymath.circle.carea(3)
rst = c.carea(3)
print( rst )
# rst = mymath.calc.cmToInch( 10 )
rst = cmToInch(10)
print( round(rst,2) ) #'%.2f'%rst
