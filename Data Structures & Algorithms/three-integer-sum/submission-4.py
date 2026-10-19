class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Sort and Initiate Return
        nums.sort()
        ret = []

        #Iterate on 1 and run 2 pointer on the remaining
        #While iterating, keep incrementing the pointer if the value matches the preivous [Avoids repeats]
        #When appending, keep incrementing pointer if the value matches the previous [Avoids repeats]
        #len(nums) == 3
        for i in range(len(nums)-2): #1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1

            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l+=1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r-=1
                else:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        #Return
        return ret