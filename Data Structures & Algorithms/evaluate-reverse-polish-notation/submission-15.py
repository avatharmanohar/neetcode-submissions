class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        o=("+","-","*","/")
        stack=[]
        for i in tokens:
            if i not in o:
                stack.append(int(i))
            else:
                b=stack.pop()
                a=stack.pop()
                if i=="+":
                    res=a+b
                elif i=="-":
                    res=a-b
                elif i=="*":
                    res=a*b
                else:
                    res=a/b
                stack.append(int(res))
        return stack[0]
