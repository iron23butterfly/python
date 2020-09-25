print('\n')

sam = {}
sam['weapon'] = 'chainsaw'
sam['10'] = 'Vishnu Avataar'
sam['sapta'] = 'rishis'
print(sam)
print(sam['sapta'])

del sam['weapon']
print(sam)

# OUTPUT
# {'weapon': 'chainsaw', '10': 'Vishnu Avataar', 'sapta': 'rishis'}
# rishis
# {'10': 'Vishnu Avataar', 'sapta': 'rishis'}
