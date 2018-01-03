#Decision Making

#1] if statements

amount = 10000
if amount>1000:
   discount = amount*0.05
   print ("Discount: ",discount)
print ("Good Bye !!!")


#2] if...Else statements

amount = int(input("Enter amount: "))

if amount<1000:
   discount = amount*0.05
   print ("Discount",discount)
else:
   discount = amount*0.10
   print ("Discount",discount)

print ("Net payable:",amount-discount)

#3] elif statements

amount = int(input("Enter amount: "))

if amount<1000:
   discount = amount*0.05
   print ("Discount",discount)
elif amount<5000:
   discount = amount*0.10
   print ("Discount",discount)
else:
   discount = amount*0.15
   print ("Discount",discount)

print ("Net payable:",amount-discount)


#4]  Nested if

num = int(input("enter number"))
if num%2 == 0:
    if num%3 == 0:
      print ("Divisible by 3 and 2")
    else:
      print ("divisible by 2 not divisible by 3")
else:
  if num%3 == 0:
      print ("divisible by 3 not divisible by 2")
  else:
      print  ("not Divisible by 2 not divisible by 3")

# Loops

#1] While loop
count = 0
while (count < 5):
   print ('The count is:', count)
   count = count + 1
print ("Done!")

#2] While loop with Else
count = 0
while count < 5:
   print (" This is {} iteration".format(count))
   count = count + 1
else:
   print (" This is last iteration")


#3] For Loops

# Example 1
for var in list(range(5)):
   print (var)


# Example 2
for letter in 'DBIT':     # traversal of a string sequence
   print ('Current Letter :', letter)
print()

# Example 3
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        			# traversal of List sequence
   print ('Current fruit :', fruit)

# Example 4
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('Current fruit :', fruits[index])

# Example 5
stud_name = ('ABC', 'LMN', 'XYZ', 'PQR')
for i, stud in enumerate(stud_name,1):
    print (i,stud)

#4] FOR with ELSE

numbers = [11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
   if num%2 == 0:
      print ('the list contains an even number')
      break
else:
   print ('the list does not contain even number')



#NESTED LOOP

for iterating_var in sequence:
   for iterating_var in sequence:
      statements(s)
   statements(s)



while expression:
   while expression:
      statement(s)
   statement(s)
