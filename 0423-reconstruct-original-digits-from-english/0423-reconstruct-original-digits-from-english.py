class Solution:
    def originalDigits(self, s: str) -> str:
        count={}
        for i in s:
            count[i]=count.get(i,0)+1

        num=[0]*10

        num[0]=count.get('z',0)
        num[2]=count.get('w',0)
        num[4]=count.get('u',0)
        num[6]=count.get('x',0)
        num[8]=count.get('g',0)

        num[3]=count.get('t',0) -num[2]-num[8]
        num[5]=count.get('f',0) - num[4]
        num[7]=count.get('s',0)-num[6]
        num[1]=count.get('o',0) -num[0]-num[2]-num[4]

        num[9] = count.get('i', 0) - num[5] - num[6] - num[8]

        result=""
        
        for i in range(10):
            result+=str(i)*num[i]

        return result
