class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        #Sorting the list
        sorted_list = sorted(nums)

        #Track current length and longest length
        current_number = sorted_list[0]
        longest_length = 1
        current_length = 1

        for item in sorted_list[1:]:
            if item == current_number:
                continue
            elif item == current_number + 1:
                current_length += 1
                current_number = item
            else:
                current_length = 1
                current_number = item

            if current_length > longest_length:
                longest_length = current_length

        return longest_length