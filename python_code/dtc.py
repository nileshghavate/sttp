

print(ord('A'))

print(chr(65))



#Example DTC To Tuple
# 1) list -> tuple
print(tuple(['pull request', 'open source', 'repository', 'branch']))

#Note: We can convert any iterable type to a tuple, including strings:

#2) string -> tuple
print(tuple('Nilesh'))
#3) string -> tuple
print(tuple('1000'))
#4) integer -> tuple    === NOT POSSIBLE
print(tuple(1000))
#5)similarly, dict is not iterable



#Example DTC To LIST

#1) tuple -> list
print(list(('CN', 'OS', 'DBMS')))

#2) String -> list

print(list('DBMS'))

#3) integer -> list    === NOT POSSIBLE
print(list(1000))
#4) similarly, dict is not iterable



#Example DTC To STRING

print(",".join(('CN', 'OS', 'DBMS')))
print(",".join(['CN', 'OS', 'DBMS']))

# updating string
var1 = list('Hello world!')
print(var1)
var1[6:11] = 'DBIT'
print ("".join(var1))



#Example DTC To  SET
print(set())
# from string
print(set('Python and python'))

# from tuple
print(set(('a', 'e', 'i', 'o', 'u')))

# from list
print(set(['a', 'e', 'i', 'o', 'u']))

# from range
print(set(range(5)))



#remove mulitple occurences
marks_regular = [11,33,55,39,55,75,37,21,23,41,13]
s = set(marks_regular)
print(s)
s.remove(55)
print(s)








#evaluate expression
# Example 1:
x = 1
print (eval('x + 1'))

# Example 2:
expr = input("Enter the function(in terms of x):")
x = int(input("Enter the value of x:"))
y = eval(expr)
print("y = {}".format(y))
