def series(n): # return Fibonacci series up to n
   result = []
   a, b = 0, 1
   while b < n:
      result.append(b)
      a, b = b, a + b
   return result


def fib(n):
   result = []
   a, b = 0, 1
   result.append(a)
   while b < n:
      result.append(b)
      a, b = b, a + b
   return result


#Executing Modules as Scripts -> uncomment foll lines
if __name__ == "__main__":
   f = series(100)
   print(f)
