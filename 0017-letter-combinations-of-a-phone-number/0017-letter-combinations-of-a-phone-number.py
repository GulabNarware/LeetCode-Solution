class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        d={
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }

        result=[]
        def sq(indx,count):

            if indx>=len(digits):
                result.append(''.join(count.copy()))
                return 

            for ch in d[digits[indx]]:

                count.append(ch)

                sq(indx+1,count)
                count.pop()

        sq(0,[])

        return result
            



            

            
        