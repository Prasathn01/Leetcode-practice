# brute force approach 
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
                
            if count == 1:
                return nums[i]

#optimal solution

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0

        for num in nums:
            result = result ^ num

        return result
        
        

        
        
        
        

        