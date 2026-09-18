class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        sum_arrt=0
        def check(n):

            count=0
            sum_ele=0

            for j in range(1,int(n**0.5)+1):

                if n%j==0:
                    other=n//j
                    count+=1
                    sum_ele+=j
                    if other != j:
                        count += 1
                        sum_ele += other

            

                if count>4:
                    return 0
            if count==4:
                return sum_ele

            return 0

        total=0

        for i in nums:
            total+=check(i)

        return total
            