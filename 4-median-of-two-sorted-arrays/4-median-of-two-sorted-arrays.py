class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = []
        num=nums1+nums2
        num.sort()
        if len(num)%2==0:
            i=len(num)//2
            return (num[i]+num[i-1])/2
        else:
            i=len(num)//2
            return num[i]