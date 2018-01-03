
#Example 1
it = [ 'cn', 'dbms' , 'os', 'coa', 4]
comp = ['cn', 1]

print (it)          # Prints complete list
print (it[0])       # Prints first element of the list
print (it[1:3])     # Prints elements starting from 2nd till 3rd
print (it[2:])      # Prints elements starting from 3rd element
print (comp * 2)  # Prints list two times
print (it + comp) # Prints concatenated lists

#Update list

it[1] = 'adbms'
print (it)          # Prints complete list

#delete list

del it[2]
print (list)


# Example 2

marks_regular = [11,33,55,39,55,75,37,21,23,41,13]
marks_diploma = [38,21,27,42,43]

print (len(marks_regular))
print(marks_regular+marks_diploma)
print (max(marks_regular))
print (marks_diploma * 2)
print (33 in marks_regular)

# Method available
marks_regular = [11,33,55,39,55,75,37,21,23,41,13]
marks_diploma = [38,21,27,42,43]

marks_regular.append(10)
print(marks_regular)
print(marks_regular.count(55))

marks_regular.extend(marks_diploma)
print(marks_regular)

print(marks_regular.index(39))

marks_regular.insert(1, 22)
print(marks_regular)

print(marks_regular.pop())      # removes element and return value

marks_regular.remove(55)
print(marks_regular)              # removes element but does not return value

marks_regular.reverse()
print(marks_regular)

marks_regular.sort()
print(marks_regular)
