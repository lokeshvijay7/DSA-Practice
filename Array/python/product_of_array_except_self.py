# LeetCode problem : 238. Product of Array Except Self
class Solution(object):
    def productExceptSelf(self,nums):
        n = len(nums)
        result = [1] * n

        p = 1
        for i in range(n):
            result[i] = p
            p *= nums[i]

        s = 1
        for i in range(n - 1, -1, -1):
            result[i] *= s
            s*= nums[i]

        return result

        