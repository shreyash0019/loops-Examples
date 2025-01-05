n= int(input("enter input number: "))
if (n<=0):
    print("enter valid input number")
else:
    if (n%2==0):
        print(n)
        n=n-1
        print("-"*50)
    for v in range (n,0,-2):
        print(v)
