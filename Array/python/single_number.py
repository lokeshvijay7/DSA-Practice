class solution() :
  def single_number(self,nums):
    i = 0
    for number in nums:
      i ^= number
    return i


nums =[3,4,3,5,6,4,5]
s = solution()
print(s.single_number(nums))
