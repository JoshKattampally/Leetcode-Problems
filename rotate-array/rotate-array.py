class Solution(object):
    def rotate(self, nums, k):
        for i in range(k % len(nums)):
            nums.insert(0, nums.pop())