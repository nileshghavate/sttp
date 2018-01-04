#Example 1

class Emp:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Emp.empCount += 1

   def __str__(self):
       print(self.name, self.salary)       # str returns and not print
       #return 'name={}, sal={}'.format(self.name,self.salary)
   def displayCount(self):
     print ("Total Employee %d" , Emp.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

e1 = Emp("abc", 7550)
e2 = Emp("lmn", 3590)

e1.displayEmployee()
e2.displayEmployee()
print ("Total Employee %d" % Emp.empCount)
print (e1)



#Built-In Class Attributes

print ("Employee.__doc__:", Emp.__doc__)
print ("Employee.__name__:", Emp.__name__)
print ("Employee.__module__:", Emp.__module__)
print ("Employee.__bases__:", Emp.__bases__)
print ("Employee.__dict__:", Emp.__dict__ )



# Accessing Attributes

print(hasattr(e1, 'salary'))
print(getattr(e1, 'salary'))
print(setattr(e1, 'salary', 7000))
print(getattr(e1, 'salary'))
delattr(e1, 'salary')
print(hasattr(e1, 'salary'))


#Class Inheritance


class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)


class Child(Parent): 		# define child class, u can add multiple parent class here
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method



#Data Hiding

class Emp:
   __empCount = 0

   def count(self):
      self.__empCount += 1
      print (self.__empCount)

c = Emp()
c.count()
c.count()
print (c.__empCount)
