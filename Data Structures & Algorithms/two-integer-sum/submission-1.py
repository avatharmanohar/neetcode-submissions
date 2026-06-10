class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            
            for j in range(1,len(nums)) :
                t=nums[i]+nums[j]
                if t==target and i!=j:
                    return [i,j]
