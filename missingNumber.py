class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort() #[0, 1, 3]
        n = len(nums) #[0, 1, 2, 3]
        original_list = []
        final_list = []
        
        for num in range(n):
            if num in nums:
                original_list.append(num)
            else:
                final_list.append(num)

        if original_list == nums:
            return n
        
        for i in final_list:
            return i
        
        

                


        