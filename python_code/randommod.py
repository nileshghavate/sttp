import random

# randrange ([start,] stop [,step])
print(random.randrange(0,100,5))

# random()                                    #0.0 <= r <= 1.0
print(random.random())

# random.shuffle(list)
l=[1, 2, 3, 5, 9]
random.shuffle(l)
print(l)


# random.uniform(5, 10)        #  returns a floating point number between 5 and 10
print (random.uniform(5,10))

# #choice() method returns a random item from a list, tuple, or string.
print ("returns a random number from range(100) : ",random.choice(range(100)))
print ("returns random element from list [1, 2, 3, 5, 9] : ",random.choice([1, 2, 3, 5, 9]))
print ("returns random character from string 'Hello World' : ", random.choice('Hello World'))
