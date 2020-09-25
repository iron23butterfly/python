
x = 'te\nst'
print (x)
x = 'te\\nst'
print (x)
print ('\n')

Vishnu = 'Lakshmi' in 'bhagyaLakshmi'
print (Vishnu)

a = str(int(2.23) + float(14)) + "tomatoes"
print (a)
print ('Ram Ram'.upper())
print ('SUPER Ham'.lower())
b = 'Tat tvam asi'
print (b)
print (b.split())
print(b.split('t'))
print(b.join(a))

print("\n")
s = 'hello'
s1 = s.replace('l','j')
print ('s1 ',s1)
s_list = list(s)
print(s_list)
s_list[2] = 'j'
print(s_list)
s_list[1] = 'a'
print(s_list)

s2 =[0]*len(s_list)
for i in range(0, (len(s_list) - 1)):
    s2[i] = s_list[i]
print('s2 ',s2)

s3 = ''.join(s_list)
print('s3', s3)

# OUTPUT
# te
# st
# te\nst
# 
# 
# True
# 16.0tomatoes
# RAM RAM
# super ham
# Tat tvam asi
# ['Tat', 'tvam', 'asi']
# ['Ta', ' ', 'vam asi']
# 1Tat tvam asi6Tat tvam asi.Tat tvam asi0Tat tvam asitTat tvam asioTat tvam asimTat tvam asiaTat tvam asitTat tvam asioTat tvam asieTat tvam asis
# 
# 
# s1  hejjo
# ['h', 'e', 'l', 'l', 'o']
# ['h', 'e', 'j', 'l', 'o']
# ['h', 'a', 'j', 'l', 'o']
# s2  ['h', 'a', 'j', 'l', 0]
# s3 hajlo
