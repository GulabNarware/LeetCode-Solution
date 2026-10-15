class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]

        for i in s:
            if i != "*":
                stack.append(i)

            if len(stack)>0 and i=="*":
                stack.pop()

        return "".join(stack)
