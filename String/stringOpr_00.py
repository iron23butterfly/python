str_1 = 'String'
str_2 = 'Operation'
print (type(str_1))
print (type(str_2))
print (str_1 +" "+ str_2)
print (str_1 ," ", str_2)
print (str_1,str_2)
print (len(str_1+str_2))
print ('Bramha Vishnu Shiva'.find('Lakshmi'))
print ('Saraswati Parvati Lakshmi'.find('Lakshmi'))
print ('Saraswati Parvati Lakshmi'.find('lakshmi'))
print ('|{:26}|'.format('26 charaters width'))
print ('|{}|'.format('26 charaters width'))
print ('|{:54}|'.format('26 charaters width'))
print ('|{:3}|'.format('26 charaters width'))

print('|1 is {} {}|'.format(8, 9))
print('|2 is {1} {0}|'.format(8, 9))
print('|3 is {0:>9} {1:10}|'.format(8, 9))

z = 10
y = "something %d" %z
print (y)
y = "somethinf %f" %z
print (y)
y = "somethinf %.2f" %z
print (y)

print('Hello, World.')
x1 = 'Ram'
y1 = 'Seeta {}'.format(x1)
print ('y1:' + y1)
z1 = f'Seeta {x1}'
print ('z1: ' + z1)
# both .format() and f' {} ' are the same

# OUTPUT
# <class 'str'>
# <class 'str'>
# String Operation
# String   Operation
# String Operation
# 15
# -1
# 18
# -1
# |26 charaters width        |
# |26 charaters width|
# |26 charaters width                                    |
# |26 charaters width|

# OUTPUT:
# |1 is 8 9|
# |2 is 9 8|
# |3 is         8          9|

# something 10
# somethinf 10.000000
# somethinf 10.00

# Hello, World.
# y1:Seeta Ram
# z1: Seeta Ram
