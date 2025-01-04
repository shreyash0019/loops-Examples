word = input("Enter any word: ")
print("-"*50)
for k in range(len(word)-1,-1,-1):
    print(word[k])
print("------ OR ------")
for k in range (-1,-len(word)-1,-1):
    print(word[k])
print("-"*50)
