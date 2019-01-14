import sys
# String Formatting
## Concatenation
name = 'winni'
age = 78

# print('my name is ' + name + ' : i am ' + str(age) + ' years old')

## Arguments by position
#print('my name is {name} : i am {age} years old'.format(name=name,age=age))

## F-Strings
#print(sys.version_info)
# print(f'my name is {name} : i am {age} years old')

# String Methods
s = 'running leopards'
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())
print('length is ' + str(len(s)))
print(s.replace('running','flying'))
print(s.count('n'))
print(s.startswith('running'))
print(s.endswith('soup'))
print(s.split())
print(s.find('p'))
print(s.isalnum())
print(s.isalpha())