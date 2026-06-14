class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        o={")":"(","]":"[","}":"{"}
        for c in s:
            if c in o:
                if stack and stack[-1]==o[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        