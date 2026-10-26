class Solution:
    def clumsy(self, n: int) -> int:
        if n==1:return 1
        # mult=[42,47,43,45]
        # res=n
        # indx=0
        # for i in range(n-1,0,-1):
        #     if indx==0:
        #         res*=i
        #     elif indx==1:
        #         res//=i
        #     elif indx==2:
        #         res+=i
        #     else:
        #         res-=i
        #     indx+=1
        #     if indx==4:
        #         indx=0
        # return res

        
        # stack=[]
        # indx=0
        # for i in range(n,0,-1):
        #     if len(stack)==0:
        #         stack.append(i)


        #     elif indx==0:
        #         a=stack.pop()
        #         temp=a*i
        #         stack.append(temp)
        #         indx+=1

        #     elif indx==1:
        #         a=stack.pop()
        #         temp=a//i
        #         stack.append(temp)
        #         indx+=1

        #     elif indx==2:
        #         stack.append(i)
        #         indx+=1

        #     elif indx==3:
        #         stack.append(-i)
        #         indx+=1

        #     if indx==4:
        #         indx=0


        # return sum(stack)

        stack=[n]
        n-=1
        indx=0
        while n>0:
            if indx==0:
                stack[-1]*=n
            elif indx==1:
                stack[-1] = int(stack[-1] / n)
            elif indx==2:
                stack.append(n)
            else:
                stack.append(-n)

            indx=(indx+1)%4

            n-=1

        return sum(stack)


            
                





