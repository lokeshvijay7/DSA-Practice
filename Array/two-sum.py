
def two_sum(n, t):
  s = {}
  for i,num in enumerate(n):
    different = t - num
    if different in s:
      return [s[different], i]
    s[num] = i
  return []
