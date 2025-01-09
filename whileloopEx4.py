n = int(input("enter number: "))
if(n<=0):
    print("Invalid input")
else:
    i = 1
while(i<=n):
        if(i%2!=0):
            print(i)
            i=i+2