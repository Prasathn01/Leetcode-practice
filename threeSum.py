# nested loops
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    total = nums[i] + nums[j] + nums[k] 
                    triplets = [nums[i], nums[j], nums[k]]
                    if total == 0:
                        if triplets not in result:
                            result.append(triplets)

#duplicate checking
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1 

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplet = [nums[i], nums[left], nums[right]]
                    if triplet not in result:
                        result.append(triplet)
                    left += 1
                    right -= 1
                    
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
                
        
#duplicate skipping
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result
