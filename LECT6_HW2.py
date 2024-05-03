users = [
    {'name': 'Luarvik L. Luarvik',
     'age': 17},
    {'name': 'Olaf Andvarafors',
     'age': 18},
    {'name': 'Brun Du Barnstokr',
     'age': 19}
]
# Result: ['Olaf Andvarafors', 'Brun Du Barnstokr']

ages = [age["age"] for age in users]
names = [name["name"] for name in users]
real_dict = dict(zip(ages, names))
allowed_users = []

for age, name in real_dict.items():
    if age >= 18:
        allowed_users.append(name)
print(allowed_users)





