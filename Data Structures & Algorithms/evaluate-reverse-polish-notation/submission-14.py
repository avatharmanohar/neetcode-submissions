class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        o=("+","-","*","/")
        
        stack=[]
        if len(tokens)==1 and tokens[0] not in o:
            return int(tokens[0])
        
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

        
        