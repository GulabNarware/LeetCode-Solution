class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        
        #slop formula=(y2-y1)/(x2-x1)
        # ya dy=(y2-y1) ,dx=(x2-x1)
        # so dy/dx
#slop is liye nikal rahe h taki pata chale ki wo point ke bich kitne ka angle h agar do slop equal a gye yani to same angle me h or ek line me h 
        result=0
        n=len(points)
        if n==1:
            return 1
        for i in range(n):
            

            for j in range(i+1,n):
                count=2

                dy=points[j][1]-points[i][1] #dy=(y2-y1)
                dx=points[j][0]-points[i][0] #dx=(x2-x1)

                #dono same h but division operator expensive hota h is liye multiple kar ke bhi check kar sakte h 
                #dy/dx == dy_/dx_
                #OR
                #dx*dy_ == dy*dx_

                #yaha par ham check kar rhe h ki kya or bhi point line me h 
                for k in range(n):
                    if k!=i and k!=j:
                        dy_=points[k][1]-points[i][1] #dy=(y3-y1)
                        dx_=points[k][0]-points[i][0] #dx=(x3-x1)

                        if dx*dy_==dy*dx_:
                            count+=1

                result=max(result,count)


        return result


