#Name:Adithi Mahendran USN:1RUA25BCA0005
#Factorial using def
def factorial (n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
n=int(input("enter a number"))
print("factorial=",factorial(n))
