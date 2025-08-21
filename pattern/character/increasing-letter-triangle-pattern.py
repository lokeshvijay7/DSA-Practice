num = int(input("Enter a number:"))
for i in range(num):
    p = 65 
    for j in range(i+1):
        print(chr(p), end="")
        p+=1
    print()    