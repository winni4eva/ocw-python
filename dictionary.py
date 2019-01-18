person = {
    'first_name': 'adam',
    'last_name': 'winni' 
}
print(type(person))

person2 = dict(first_name='fred',last_name='droid')
print(person2)
print(person['first_name'])
print(person.get('last_name'))

person['phone']='0245678999'
print(person)

print(person.keys())
print(person.items())

person3 = person.copy()
person3['city'] = 'Accra'
print(person3)

del(person['phone'])
print(person)

#list of dict
people = [
    {'name': 'martha', 'age': 23},
    {'name': 'winni', 'age': 34}
]
print(people)