class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        length=0

        sec=0

        d={}
        if len(s)==0:
            return 0

        for f in range(len(s)):

            if s[f] not in d:
                d[s[f]]=1

                if f-sec>length:
                    length=f-sec

            else:

                while s[f] in d:
                    d.pop(s[sec])
                    sec+=1
                    
                if s[f] not in d:
                    d[s[f]]=1

        if length==0:
            return 1

        return length+1


                    

