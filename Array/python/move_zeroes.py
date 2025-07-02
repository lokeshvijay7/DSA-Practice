class Solution:
  def mz (self, nums):
    value = 0
    for j in range(len(nums)):
      if nums[j] != 0:
        nums[value] = nums[j]
        value += 1

    for i in range(value, len(nums)):
      nums[i] = 0


  
nums = [0, 1, 0, 3, 12]
mz = Solution()
mz.mz(nums)
print("After moving zeroes:", nums)
