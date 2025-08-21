num = int(input("Enter a number:"))

for i in range(num-1):
    for j in range(i+1):
        print("*", end=" ")
    print()    
    
for i in range(num):
    for j in range(i, num):
        print("*", end=" ")
    print()



# *         
# * *       
# * * *     
# * * * *   
# * * * * * 
# * * * *   
# * * *     
# * *       
# *      