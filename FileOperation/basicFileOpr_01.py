str1 = "SriGaneshaayaNamaha\nSrRamajayam"
str3 = "------------------------------"

name = input('Enter your name')
str2 = "hello {}!!! My name is Iron23Butterly".format(name)
list_str = str2.split('!')
print (list_str)

# Context Manager
with open('Ganesha.txt', 'w') as wf:
    wf.write(str3)
    wf.write(str1)
    wf.write('\n')
    len_list_str2 = len(list_str)
    print (len_list_str2)
    for lines in range(0,len_list_str2):
        if (list_str[lines]==''):
            pass
        else:
            wf.write(list_str[lines]+'!\n')
    wf.write(str3)

# OUTPUT
# Enter your name Iron23Butterfly
# ['hello  Iron23Butterfly', '', '', ' My name is Sandhya Ram']
# 4
