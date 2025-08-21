num = int(input("enter a number:"))
for i in range(num):
    for j in range(i,num):
      print(' ', end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()    