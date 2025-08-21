num = int(input("Enter a number:"))
p = 65

for i in range(num):
    for j in range(i+1):
       print(chr(p), end=" ")
    p+=1
    print()       