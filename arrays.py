myArray = [1, 'string', 1, 2.34, True, False]
myArray2 = list((1,2,3,4))

print(type(myArray), type(myArray2))

print(myArray[0])
print(len(myArray2))
myArray.append('winni')
print(myArray)
myArray.remove('string')
print(myArray)