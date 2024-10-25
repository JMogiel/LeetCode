class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # Initialize the slow pointer
        slow = 2

        # Iterate with the fast pointer
        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1

        # Return the new length of the array with double elements
        return slow