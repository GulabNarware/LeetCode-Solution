class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]

        bracket=[""]*(n*2)

        def solve(ind,total):

            if ind>=len(bracket):
                if total==0:
                    result.append("".join(bracket))

                return 

            if total<0:
                return

            elif total>len(bracket)//2:
                return 

            bracket[ind]="("
            sum_ele=total+1

            solve(ind+1,sum_ele)

            bracket[ind]=")"
            sum_ele=total-1

            solve(ind+1,sum_ele)

        solve(0,0)
        return result