class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        m=0
        
        while i<len(prices)-1:
            j=i+1
            while j<len(prices):
                p=prices[j]-prices[i]
                m=max(m,p)
                j+=1
            i+=1
        return m

        