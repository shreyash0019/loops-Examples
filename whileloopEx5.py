n = int(input("Enter Number: "))
if(n<=0):
    print("enter valid number")
else:
    i = n
    while(i>1):
        if(n%2==0):
            print(i)
            i=i-2