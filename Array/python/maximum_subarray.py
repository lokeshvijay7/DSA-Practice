class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]       
        current_sum = 0          

        for num in nums:
            current_sum += num  

            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0

        return max_sum

            