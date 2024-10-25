class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # Slow pointer - keeps track of the position where the next unique elements
        # should be placed

        slow = 0 # indexing starts at 0

        # Fast pointer - iterate through the list looking for unique numbers
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        # Return new array with unique elements
        return slow + 1
