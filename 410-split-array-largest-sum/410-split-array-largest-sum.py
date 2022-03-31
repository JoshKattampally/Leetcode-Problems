class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(partial_sum: List[int], try_sum: int, m: int) -> int:
            n = len(partial_sum)
            cur_sum = 0
            cur_id = 1
            for _ in range(n):                
                if partial_sum[_] - cur_sum <= try_sum:
                    continue
                else:
                    cur_sum = partial_sum[_ - 1]
                    cur_id += 1
                    if cur_id > m:
                        return False
            return True
        
        lower = max(nums) - 1
        upper = sum(nums)
        n = len(nums)
        t = 0
        partial_sum = []
        for i in range(n):
            t += nums[i]
            partial_sum.append(t)
            
        while upper - lower > 1:
            tmp = (upper + lower) // 2
            if check(partial_sum, tmp, m):
                upper = tmp
            else:
                lower = tmp
        return upper