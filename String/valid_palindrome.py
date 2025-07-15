class Solution(object):
    def isPalindrome(self, s):
        clean_string = ""
        for char in s:
            if char.isalnum():
                lower_case = char.lower()
                clean_string += lower_case
        reversed_string = clean_string[::-1]
        if reversed_string == clean_string:
            return True
        else:
            return False

                


s = "A man, a plan, a canal: Panama"
solution = Solution()
solution.isPalindrome(s)
