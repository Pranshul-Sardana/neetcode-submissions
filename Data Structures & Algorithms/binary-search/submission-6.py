class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #Initate the pointers
        l_ptr = 0
        r_ptr = len(nums) - 1

        #Iterate if the current pointer is not equal the left or the right pointer
        while l_ptr <= r_ptr:
            c_ptr = l_ptr + (r_ptr-l_ptr)//2
            #print(f"{c_ptr = }, {nums[c_ptr] = }")

            #Sample value at the middle ptr and compare with targer
            #If value found, return the sampled index
            if nums[c_ptr] == target:
                return c_ptr
            
            #Move left, right, and center pointer based on the comaprison
            elif nums[c_ptr] < target:
                l_ptr = c_ptr + 1
            elif nums[c_ptr] > target:
                r_ptr = c_ptr - 1

        #If no sample found, return -1
        return -1