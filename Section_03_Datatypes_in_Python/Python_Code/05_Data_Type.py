print("#################### LIST DATA TYPE ####################")

list1 = [1, 2, 3, 4, 5, 'aviral']
print(type(list1))
print(list1)
print(list1[0])
print(list1[-1])
list1.append(50)
print(list1)
print(type(list1))

print("#################### TUPLE DATA TYPE ####################")

tuple1 = (1, 2, 3, 4, 5, 'aviral')
print(type(tuple1))
print(tuple1)

tuple2 = ()

print(tuple2)
print(type(tuple2))

print("#################### SET DATA TYPE ####################")

set1 = {1, 2, 3, 4, 5, 'aviral'}
print(type(set1))
print(set1)
set1.add(50)
set1.remove(1)
print(set1)

print("#################### FROZENSET DATA TYPE ####################")

set1 = {1, 2, 3, 4, 5, 'aviral'}
frozenset1 = frozenset(set1)
print(type(frozenset1))
print(frozenset1)

print("#################### DICTIONARY DATA TYPE ####################")

dict1 = {'name': 'Aviral', 'age': 20, 'city': 'New Delhi'}
print(type(dict1))
print(dict1)

dict1[20] = 'twenty'
print(dict1)

print("#################### RANGE DATA TYPE ########################")

range1 = range(10)
print(type(range1))

for x in range1:
    print(x)

range2 = (10, 50, 3)
for x in range2:
    print(x)

print("#################### BYTES AND BYTE ARRAY DATA TYPE ####################")

bytes1 = [65, 66, 67, 68, 69]
byt = bytes(bytes1)
print(type(byt))
print(byt)
