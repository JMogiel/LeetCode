class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farthest = 0
        for i in range(len(nums)):
            # If we are at an index that is not reachable, return False
            if i > farthest:
                return False
            # Update the farthest we can reach from this position
            farthest = max(farthest, i + nums[i])
            # If we can reach or exceed the last index, return True
            if farthest >= len(nums) - 1:
                return True
        return False
