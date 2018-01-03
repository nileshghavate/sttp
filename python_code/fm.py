#Functions

#Example 1

def welcome_func():
    print ("Welcome to Python Function");
    return
welcome_func()



#Example 2  -passing argument by reference and by value...... its only reference
def welcome_func(name):
   #name ='Participant'
    print ("Welcome {} to Python Function".format(name));
    return

name= "Nilesh"
welcome_func(name)
print("Outside Function:",name)


#Add docstring
""" This function is to welcome user  """

#Keyword Argument
def printme(name, str ):
   "This prints a passed string into this function"
   print (str, name)
   return
printme( str = "My name is", name = "Nilesh")

#Default Argument
def printme( str, name = 'noname', age ='25' ):
        print("string:",str," and name:",name," and age:",age)
        return
printme( str = "Python", name = "Nilesh")
printme( str = "Python3")

#Variable length Argument

def printme(*name):
   "This prints a variable passed arguments"
   for var in name:
      print (var)
   return
printme("python")
printme("py", "k","a","i")





#Anonymous Functions
#lambda Example 1

sum = lambda arg1, arg2: arg1 + arg2

print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))


#lambda Example 2

x = [11,33,55,39,55,75,37,21,23,41,13]
print(list(filter(lambda a: a != 55, x)))




#Modules
a) check  series.py
b) use use.py

#Executing Modules as Scripts
