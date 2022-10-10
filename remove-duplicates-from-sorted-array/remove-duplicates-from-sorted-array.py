class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            
            if(i == len(nums)-1):
                break
                
            while(i < len(nums) -1 and nums[i] == nums[i+1]):
                nums.pop(i+1)
                
            