# Using enumerate function for index and elem in one for 
s = 'Hello'
for idx, elem in enumerate(s):
    print(idx, elem)


# Using method items for dictionary key and value
city = {
    'Chita': 'Russia',
    'Nsk': 'Russia',
    'Msk': 'Russia',
}

for key, value in city.items():
    print(key, value)


# Using | and & with set

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2, s1 & s2)
