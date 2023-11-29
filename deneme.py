"""
yukseklik=5
def draw_triangle(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        print()
draw_triangle(yukseklik)
"""
"""
import random
print(random.randint(1,10))
print(random.randrange(1,10))
"""
"""
import random
random.seed(2)
print(random.random())
"""
"""
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
"""
"""
def fib(n):
   if n==0:
      return 0
   elif n==1:
      return 1
   else:
      return fib(n-1)+ fib(n-2)
for n in range(10):
    a=fib(n)
    print(a)
 """
"""
def gcd(x,y):
    if x%y==0:
       return y
    else:
       return gcd(x,x%y)
a=gcd(x,y)
print(a)
"""
"""
def main():
    outfile= open("philisophers.txt","w")
    outfile.write("john locke\n")
    outfile.write("david hume\n")
    outfile.write("edmund burke\n")
    outfile.close()
main()
"""