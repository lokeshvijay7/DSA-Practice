num = int(input("Enter a number: "))
for i in range(1, num + 1):
  for j in range(i):
    print("*", end=" ")
  print()
  
# *         
# * *       
# * * *     
# * * * *   
# * * * * * 