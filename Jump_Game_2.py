class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Vars to keep track of made jumps, how far can we jump
        made_jumps = 0
        current_end = 0
        farthest = 0

        # Edge case where list has one or fewer elements
        if len(nums) <= 1:
            return 0

        # Iterating through list without last element
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                made_jumps += 1
                current_end = farthest

                if current_end >= len(nums) - 1:
                    return made_jumps

        return made_jumps
