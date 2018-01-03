#Example 1 :

dict = {}
print (dict)

dict['one'] = "This is one"
dict[2]     = "This is two"
print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key

print (dict)


#Example 2 :

stud = {'name': 'john','roll':6734, 'dept': 'it'}
print (stud)         		# Prints complete dictionary

#Update dict

stud['roll'] = 8759; 		# update existing entry
stud['college'] = "DBIT " 	# Add new entry

#Methods for dictionary object

print (stud)
print (stud['roll'])  # Prints specific values
print (stud.keys())   # Prints all the keys
print (stud.values()) # Prints all the values
print (stud.items())  # Prints all the key-values as tuple
print (stud.get('university','MUMBAI'))   # second is default value
print ('roll'in stud)

college_copy = stud.copy()
print ("College_Record: ",college_copy)

#delete operation

del stud['name']          # remove entry with key 'name'
print (stud)
stud.clear() # remove all entries in dict
print (stud)           # delete entire dictionary


# Properties of Dictionary Keys
#
# (a) More than one entry per key is not allowed. This means no duplicate key is allowed. When duplicate keys are encountered during assignment, the last assignment wins.
# (b) Keys must be immutable. This means you can use strings, numbers or tuples as dictionary keys but something like ['key'] is not allowed.

dict = {['Name']: 'Zara', 'Age': 7, 45: 23, (22,66) : 'two'}
print (dict)
