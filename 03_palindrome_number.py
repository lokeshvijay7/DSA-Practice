

def pd (x) :
  if(x < 0) :
    return False  
  if (x !=0) :

    return False
  if (0 <= x < 10):
    return True
  if (x % 10 == 0) :
    return False
  r = 0
  while x > r:
    r = r * 10 + x % 10
    x //= 10  
  return x == r or x == r // 10

x = int(input("Enter a number: "))
print("palindrome:", pd(x))