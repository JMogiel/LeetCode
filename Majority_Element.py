from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        counter = Counter(nums)
        most_common_ele = counter.most_common(1)
        element, count = most_common_ele[0]
        return element
