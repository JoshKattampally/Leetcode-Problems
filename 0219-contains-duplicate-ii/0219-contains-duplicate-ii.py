class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        for index, num in enumerate(nums):
            if num in dict:
                if(abs(index - dict[num]) <= k):
                    return True
                else:
                    dict[num] = index
            else:
                dict[num] = index
        return False