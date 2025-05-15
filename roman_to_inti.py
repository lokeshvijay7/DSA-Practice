def rom(s) :
  roman = {
   'I':1,
   'V':5,
   'X':10,
   'L':50,
   'c':100,
   'D':500,
   'M':1000

  }

  t = 0
  pre = 0

  for char in reversed(s) :
    current = roman[char]
    if current < pre:
      t = t - current
    else:
      t = t + current 
      pre = current
  return t 
    
print(rom("III"))   
print(rom("LVIII"))    
