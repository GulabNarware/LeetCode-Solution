class Solution:
    def isValid(self, s: str) -> bool:
        d={")":"(",
        "]":"[",
        "}":"{"}

        stack=[]

        for i in s:
            if i not in d:
                stack.append(i)

            else:
                if i in d:

                    if len(stack)!=0 and d[i]==stack[-1]:
                        stack.pop()

                    else:
                        return False

        return  len(stack)==0 





