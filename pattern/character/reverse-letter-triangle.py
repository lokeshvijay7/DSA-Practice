num = int(input("Enter a number:"))
for i in range(num):
    p = 65
    for j in range(i, num):
       print(chr(p), end=" ")
       p+=1
    print()       