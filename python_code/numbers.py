#Python Numbers

a = b = c = 1
print (a)
print (b)
print (c)

a,b,c = 1,2,'dbit'
print (a)
print (b)
print (c)

del a,b,c
print (a)
print (b)
print (c)

#Number Type Conversion

number = '32'
print (number)
print(type(number))
x=int(number)
print(x)
print(type(x))


number = 32
print (number)
print(type(number))
x=float(number)
print(x)
print(type(x))

number = 32
print (number)
print(type(number))
x=complex(number)
print(x)
print(type(x))


number = 0xA0F
print (number)
print (hex(number))
print (oct(number))
print (bin(number))



number = int('1000',2)
print (number)
print (hex(number))
print (oct(number))
print (bin(number))

# Methods for Numbers
# abs(x)
#round(x [,n])
# pow(x, y)
# cmp(x, y)   ->  (x>y)-(x<y)
# max(x1, x2,...)
# min(x1, x2,...)

print(abs(-10))

#Following need Math Module for foll Methods
# exp(x)
# ceil(x)
# floor(x)
# log(x)
# log10(x)
# modf()  -returns the fractional and integer parts of x
# sqrt(x)

import math
print((2.3))
