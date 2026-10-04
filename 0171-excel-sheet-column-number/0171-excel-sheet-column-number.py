class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        #example:- "ABC"

        # formula :- A*26^2 + B*26^1 + C*26^0

        total=0
        power=0
        for i in range(len(columnTitle)-1,-1,-1):
            value=ord(columnTitle[i])-64

            total+=(26**power*value)
            power+=1


        return total
