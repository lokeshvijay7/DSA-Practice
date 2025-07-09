class Solution(object):
    def jump(self, nums):
        n = len(nums)
        x = 0  
        y = 0    
        z = 0 

        for i in range(n - 1):  
            y = max(y, i + nums[i])

            if i == z:
                x += 1
                z = y

        return x

        