#Bitwise Operators
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
print ('a=:',bin(a),'b=:',bin(b))
c = 0

c = a & b;        # 12 = 0000 1100
print ("result of AND is ", c,':',bin(c))

c = a | b;        # 61 = 0011 1101
print ("result of OR is ", c,':',bin(c))

c = a ^ b;        # 49 = 0011 0001
print ("result of EXOR is ", c,':',bin(c))

c = ~a;           # -61 = 1100 0011
print ("result of COMPLEMENT is ", c,':',bin(c))

c = a << 2;       # 240 = 1111 0000
print ("result of LEFT SHIFT is ", c,':',bin(c))

c = a >> 2;       # 15 = 0000 1111
print ("result of RIGHT SHIFT is ", c,':',bin(c))

print (c)
print (bin(c))



#MEMBERSHIP OPERATOR
a = 10
b = 20
c = b/a
list = [1, 2, 3, 4, 5 ]

print (a in list)
print (b in list)
print (c in list)


#Identity Operators ( IS and IS NOT) and Reference Count
a= 60
b= 10
c= 30-20
print ( a is b)
print ("id of a: ",id(a) ,"and id of b:",id(b))
print ( b is c)
print ("id of b: ",id(b) ,"and id of c:",id(c))
import sys
print("ref count for a: ",sys.getrefcount(a))
print("ref count for b: ",sys.getrefcount(b))
print("ref count for c: ",sys.getrefcount(c))

del c
print("ref count for a: ",sys.getrefcount(a))
print("ref count for b: ",sys.getrefcount(b))
print("ref count for c: ",sys.getrefcount(c))
