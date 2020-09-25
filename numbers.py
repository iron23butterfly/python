print(f'7/3 = {7/3}')
print(f'7//3 = {7//3}')

from decimal import *

a = Decimal('.10')
b = Decimal('.30')
result = a + a + a - b
print (result)
print (0.10 + 0.10 + 0.10 - 0.30)

# OUTPUT
# 7/3 = 2.3333333333333335
# 7//3 = 2
# 0.00
# 5.551115123125783e-17
