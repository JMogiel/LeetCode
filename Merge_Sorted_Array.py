class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if n == 0:
            return

        pointer_nums1 = m - 1
        pointer_nums2 = n - 1
        pointer_merged = m + n - 1

        while pointer_nums1 >= 0 and pointer_nums2 >= 0:
            if nums1[pointer_nums1] > nums2[pointer_nums2]:
                nums1[pointer_merged] = nums1[pointer_nums1]
                pointer_nums1 -= 1
            else:
                nums1[pointer_merged] = nums2[pointer_nums2]
                pointer_nums2 -= 1

            pointer_merged -= 1

        while pointer_nums2 >= 0:
            nums1[pointer_merged] = nums2[pointer_nums2]
            pointer_nums2 -= 1
            pointer_merged -= 1
