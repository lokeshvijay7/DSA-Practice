# Leetcode problem : 66. Plus One
class Solution(object):
    def plusOne(self, digits):
        digits_length = len(digits)
        for i in range(digits_length-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else :
                digits[i] = 0
        return [1] + [0]*digits_length    


 
        

digits = [1,2,3]
print(Solution().plusOne(digits))        