class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]

        for i in s:
            if len(stack)==0:
                stack.append(i)
            elif i != stack[-1] :
                stack.append(i)

            else:
                while len(stack)>0 and stack[-1]==i  :
                    stack.pop()

        return "".join(stack)

        