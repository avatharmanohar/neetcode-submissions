class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c={}
        l=0
        m=0
        res=0
        for r in range(len(s)):
            c[s[r]]=1+c.get(s[r],0)
            m=max(m,c[s[r]])
            while (r-l+1)-m>k:
                c[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
        