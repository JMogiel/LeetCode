class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        length = len(nums)

        if length <= k:
            new_k = k % length
            sub_list = nums[length - new_k:]
            nums[:0] = sub_list
            new_length = len(nums)
            del nums[new_length - new_k:]

        else:
            sub_list = nums[length - k:]
            nums[:0] = sub_list
            new_length = len(nums)
            del nums[new_length - k:]
