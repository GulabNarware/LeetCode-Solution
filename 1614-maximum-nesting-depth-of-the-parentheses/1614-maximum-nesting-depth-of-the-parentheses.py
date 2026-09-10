class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth=0
        depth=0
        for i in s:

            if i=="(":
                depth+=1

            elif i==")":
                if max_depth<depth:
                    max_depth=depth
                    depth-=1

                else:
                    depth-=1

        return max_depth
            