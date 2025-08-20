# https://www.geeksforgeeks.org/problems/triangle-pattern-1661493231/1

num = int(input("Enter a number:"))
for i in range(num):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, num-1):
        print("*", end=" ")
    for j in range(i, num):
        print("*", end=" ")
    
        
    print()    


  # * * * * * * * * *    
  #   * * * * * * *      
  #     * * * * *        
  #       * * * 
  #         * 