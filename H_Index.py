class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        h_index = 0  # Initialize var h-index

        # Sort list in descending order
        sorted_citations = sorted(citations, reverse=True)
        citations_length = len(sorted_citations)  # Take length of list

        # Loop through whole list (Paper 1: 10 it is >= 1, ..., Paper 4: 4 it is >= 4,
        # Paper 5: 3 it is not >= 5
        for i in range(citations_length):
            if sorted_citations[i] >= i + 1:
                h_index = i + 1
            else:
                pass

        return h_index
