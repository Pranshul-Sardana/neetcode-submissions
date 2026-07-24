class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)

        triplets_list = []

        for i in range(len(nums_sorted)):
            nums_i = nums_sorted[i]

            j = i + 1
            k = len(nums_sorted) - 1

            while j < k:
                nums_j = nums_sorted[j]
                nums_k = nums_sorted[k]

                number_sums = nums_i + nums_j + nums_k

                if number_sums < 0:
                    j += 1
                elif number_sums > 0:
                    k -= 1
                else:
                    j += 1
                    if [nums_i, nums_j, nums_k] not in triplets_list:
                        triplets_list.append([nums_i, nums_j, nums_k])

        return triplets_list

                
