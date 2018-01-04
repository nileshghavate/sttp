#The open Function
# Example 1  write mode
fo = open("gen.txt", "w")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.write( "Python is a great language.\nYeah its great!!\n")
fo.close()

# Exmaple 2   - read write mode
fo = open("gen.txt", "r+")
str = fo.read()
print ("Read String is : ", str)
# Check current position
position = fo.tell()
print ("Current file position : ", position)

fo.write("This is new line")
fo.seek(6,0)

fo.write(" This is second new line ")

str = fo.read()
print ("Read String is : ", str)

fo.close()


# Exmaple 3   - read  mode
fo = open("gen.txt", "a")
fo.write("This is new line")
fo.close()


# Example 4 -  Updating Metadata
# import os
# os.rename( "test1.txt", "test2.txt" )
# os.remove("text2.txt")
# os.mkdir("newdir")
# os.getcwd()               # displays the current working directory
# os.chdir("/home/dbit/")   #method to change the current directory
# os.rmdir('dirname')
