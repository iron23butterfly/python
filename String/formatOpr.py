print('|1 is {} {}|'.format(8, 9))
print('|2 is {1} {0}|'.format(8, 9))
print('|3 is {0:>9} {1:10}|'.format(8, 9))
print('|4 is "{0:>9}" "{1:10}"|'.format(8, 9))
print('|5 is "{0:>09}" "{1:010}"|'.format(8, 9))
x, y = 19, 43
print('|6 is "{0:>09}" "{1:010}"|'.format(x, y))
print('|7 is "{1:>09}" "{0:010}"|'.format(x, y))
 # Another way to do this 
print(f'|7 is "{y:>09}" "{x:010}"|')

# OUTPUT:
# |1 is 8 9|
# |2 is 9 8|
# |3 is         8          9|
# |4 is "        8" "         9"|
# |5 is "000000008" "0000000009"|
# |6 is "000000019" "0000000043"|
# |7 is "000000043" "0000000019"|
# |7 is "000000043" "0000000019"|