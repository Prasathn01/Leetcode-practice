#brute force approach 
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        final_list = []
        nums.sort()
        for i in range(len(nums)): # 0 1 2 
            for j in range(i + 1, len(nums)): # 1, 2
                if nums[i] == nums[j]:
                    final_list.append(nums[i])

        return final_list


#optimal solution using set and list approach 

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        seen = {}
        final_list = []

        for num in nums:
            if num in seen:
                if num not in final_list:
                    final_list.append(num)
            else:
                seen[num] = True
        
        return final_list
        

