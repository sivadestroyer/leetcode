# leetcode
# number of trailing zeroes in factorial
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        z=0
        if n<5:
            return 0
        while(n>=5):
            n//=5
            z+=n
        return z
