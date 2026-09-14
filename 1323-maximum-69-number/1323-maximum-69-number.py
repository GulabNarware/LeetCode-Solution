class Solution:
    def maximum69Number (self, num: int) -> int:
        l=[]

        for i in str(num):
            l.append(int(i))
        count=1
        sum_num=0
        for j in range(len(l)):

            if count ==1 and l[j]==6:
                l[j]=9
                count-=1

            sum_num=sum_num*10+l[j]


        return sum_num
                
