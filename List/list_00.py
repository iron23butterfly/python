x = []
print (x)

x = ['string', 1, 3.6]
print(x)

x.append('append_adds_EOL')
print(x)

x.insert(0, 'insert_wherever')
print(x)

x.insert(3, 777)
print(x)

x.pop(0)
print(x)

print(len(x))

y = 'splitting_a_string'
y_list = list(y)
print (y)
print (y_list)

# OUTPUT
# []
# ['string', 1, 3.6]
# ['string', 1, 3.6, 'append_adds_EOL']
# ['insert_wherever', 'string', 1, 3.6, 'append_adds_EOL']
# ['insert_wherever', 'string', 1, 777, 3.6, 'append_adds_EOL']
# ['string', 1, 777, 3.6, 'append_adds_EOL']
# 5
# splitting_a_string
# ['s', 'p', 'l', 'i', 't', 't', 'i', 'n', 'g', '_', 'a', '_', 's', 't', 'r', 'i', 'n', 'g']
