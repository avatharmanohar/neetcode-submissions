class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=[]
        v=set()
        for i in range(len(strs)):
            if i in v:
                continue
            ans=[]
            c=Counter(strs[i])
            ans.append(strs[i])
            v.add(i)
            for j in range(i+1,len(strs)):
                cn=Counter(strs[j])
                if c==cn and j not in v :
                    ans.append(strs[j])
                    v.add(j)
            l.append(ans)
        return l
                
                