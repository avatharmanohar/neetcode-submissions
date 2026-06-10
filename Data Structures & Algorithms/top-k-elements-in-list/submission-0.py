class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        f=Counter(nums)
        for key,value in f.most_common(k):
            ans.append(key)
        return ans




            
        