class solution:
    def twoSum(nums, target):
        for i in range(len(nums)): #4 
            for j in range(i + 1, len(nums)): # 0123
                if nums[i] + nums[j] == target:
                    return[i , j]

obj = solution()
print(solution.twoSum(nums = [2, 7 , 11, 15], target = 9))











'''Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].'''