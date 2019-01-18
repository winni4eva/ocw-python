def sayHello(name = 'John'):
    print(f'Hi {name}')

sayHello('adam')
sayHello()

#anonymous function / arrow functions in js
NAMS = lambda NAM1, NAM2: NAM1 * NAM2

print(NAMS( 1, 2))