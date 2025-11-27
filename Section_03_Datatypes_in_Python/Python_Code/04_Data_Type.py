string1 = 'aviral'
print(string1[3])

print('#################################')

string2 = 'abcdefghijkl'
print(string2[1:5])

print('#################################')

string3 = "aviralisagoodboy"

print(string3[0].upper() + string3[1:])
print(string3[0].upper() + string3[1:len(string3) - 1] + string3[-1].upper())

print('#################################')

floattoint = int(12.3)
print(floattoint)
print(type(floattoint))

print('#################################')

inttofloat = float(12)
print(inttofloat)
print(type(inttofloat))

print('#################################')

complexconversion = complex(2)
print(complexconversion)
print(type(complexconversion))

print('#################################')

first1 = 10
first2 = first1 + 1

print(first1, first2)
print(id(first1), id(first2))

print('#################################')

av = 10
bd = 10

print(id(av), id(bd))
print(av is bd)
