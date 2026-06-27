class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        comb={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }


        result=[]

        def backtrack(ind,subset):
            if ind>=len(digits):
                result.append("".join(subset))
                return

            for ch in comb[digits[ind]]:
                subset.append(ch)

                backtrack(ind+1,subset)
                subset.pop()


        backtrack(0,[])

        return result

