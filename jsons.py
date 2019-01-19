import json

user = '{"name": "adam", "age": "23", "email":"adams4lyf@gmail.com"}'

userJson = json.loads(user)

print(userJson)
print(userJson['name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJson = json.dumps(car)
print(carJson)