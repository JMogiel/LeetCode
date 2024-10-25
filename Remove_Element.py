class Solution(object):
    def removeElement(self, nums, val):
        # Iterating thorugh list without built-in functions
        i = 0
        for n in nums:
            if n != val:
                nums[i] = n
                i += 1
        return i
