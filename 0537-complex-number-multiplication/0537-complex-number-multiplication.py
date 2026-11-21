class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:

        eq1_a,eq1_b=num1.split("+")
        eq2_a,eq2_b=num2.split("+")

        eq1_a=int(eq1_a)
        eq2_a=int(eq2_a)

        eq2_b=eq2_b.replace("i","")
        eq2_b=int(eq2_b)

        eq1_b=eq1_b.replace("i","")
        eq1_b=int(eq1_b)


        #formula:- 
        #for real num:- ac−bd
        #for imaginiry :-ad+bc

        real=eq1_a*eq2_a-eq1_b*eq2_b
        ima=eq1_a*eq2_b+eq1_b*eq2_a

        return f"{real}+{ima}i"


