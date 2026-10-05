class Solution:
    def convertToBase7(self, num: int) -> str:
        
        is_negtive=False

        if num<0:
            num=-num
            is_negtive=True

        if num==0:
            return "0"
        result=""
        while num>0:
            rem=num%7
            num//=7
            result=str(rem)+result

        if is_negtive:
            return "-"+result

        return result


        
