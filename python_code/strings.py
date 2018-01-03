
str = 'Hello World!'
print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str[:5])      # Prints string till 4th character
print (str[0::2])     # Prints character at even places
print (str * 2)      # Prints string two times
print (str[-1])      # Prints character from end
print (str + "TEST") # Prints concatenated string
print ('H' in str)

#String Formatting Operator
print ("My name is {} and id is {} .".format('Nilesh', 70))
print ("My name is %s and id is %d ." % ('Nilesh', 70))


#Triple Quotes
para_str = """this is a long string that is made up of
several lines with TAB ( \t ) and NEWLINEs [ \n ] is displayed.
"""
print (para_str)

#Alt way to print raw string
print ('C:\\nowhere')    # outputs C:\nowhere
print (r'C:\\nowhere')   # outputs C:\\nowhere




#Built-In String Methods
str = "Find the substring and comapare with other string, if matches generate new string "
print (len(str))
print (max (str))   # max alphabetical character from the string str
print(str.capitalize())
print (str.upper())
#str.center(width[, fillchar])
print(str.center(100, '*')) # width of output string, fillchar is char to be appended
#str.count(sub, start = 0,end = len(string))
print(str.count('string',0,len(str)))
print(str.isalnum())
print(str.isdigit())
print(str.islower())
#str.replace(old, new[, max])
print(str.replace('string', 'number', 1))
print(str.split(' ', 2))   # slipt for two instance of delimiter
