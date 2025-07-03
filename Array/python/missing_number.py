def missing_number(nums):
    n = len(nums)
    total = n*(n+1)//2
    m = sum(m)
    return total - m
nums = [0, 1, 2, 3, 5]
s = missing_number(nums)
print(s) 
