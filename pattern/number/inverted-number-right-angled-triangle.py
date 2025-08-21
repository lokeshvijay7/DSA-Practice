num = int(input("Enter a number:"))
for i in range(num):
  p = 1
  for j in range(i,num):
    print(p, end=" ")
    p += 1
  print()  
