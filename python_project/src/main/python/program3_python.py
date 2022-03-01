# 3. write a program to print fibonacci series upto given number using a user defined function?

def fib(n):
   sum = 0
   a = 0
   b = 1
   mylist=[]
   for i in range(1,n):
       mylist.append(a)
       sum= a + b
       a = b
       b = sum
   print(mylist)

f = int(input("Enter number of terms to print Fibonacci series: "))
fib(f)
