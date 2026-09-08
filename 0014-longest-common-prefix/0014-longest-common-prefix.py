class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result=""
        base=strs[0]
        for i in range(0,len(base)):

            for char in strs:

                if i>=len(char) or char[i]!=strs[0][i]:
                    return result

            result+=base[i]
            
        return result


