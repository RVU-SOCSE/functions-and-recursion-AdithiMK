#Name:Adithi Mahendran
#USN:1RUA25BCA0005
def fib(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        a=b
        b=a+b
n=int(input("enter number:"))
fib(n)
