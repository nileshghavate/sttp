# Exception Handling

import time
try:
    fo = open("gen.txt", "w")
    fo.write( "Python is a great language.\nYeah its great!!\n")
    print("READ:",fo.read())
except IOError:
    print ("Error: can\'t find file or read data")
    localtime=time.time()
    fo.write ("Someone tried to read data at {} ".format(localtime))
else:
    print ("Written content in the file successfully")
fo.close()



# Example 2

import time
try:
    fo = open("gen.txt", "w")
    fo.write( "Python is a great language.\nYeah its great!!\n")
    print("READ:",fo.read())
else:
    print ("Written content in the file successfully")
fo.close()

# Example 3

import time
try:
    fo = open("gen.txt", "w")
    fo.write( "Python is a great language.\nYeah its great!!\n")
    print("READ:",fo.read())
finally:
    print ("Written content in the file successfully")
fo.close()
