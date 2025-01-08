n= int(input("Enter number until you want to find even numbers: "))
if (n<=0):
    print("{} is invalid .format(n)")
else:
    i = 2
    while (i<=n):
        if(i%2==0):
            print(i)
            i+=2


