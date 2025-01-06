n = int(input("enter number: "))
if (n<=0):
    print("enter vallid value")
else:
    prod = 1
for i in range (1,n+1):
    prod = prod*i
else:
    print(f"prod of {n}= {prod}")

print("-"*50)

line = input("Enter a line of text: ")
print(f"Given line = {line}")

noa = 0
for ch in line:
    if ch.isalpha():
        noa += 1

print(f"Number of alphabets = {noa}")
