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
z = 10
y = "something %d" %z
print (y)
y = "somethinf %f" %z
print (y)
y = "somethinf %.2f" %z
print (y)

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
# something 10
# somethinf 10.000000
# somethinf 10.00
