class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l=[]
        for num in nums:
            if num in l:
                return num
            else:
                l.append(num)
        