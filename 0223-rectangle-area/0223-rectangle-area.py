class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        #area calculation of First Reactangle

        a_len=ax2-ax1

        a_h=ay2-ay1

        area_of_a=a_len*a_h

        #area calculation of Second Reactangle

        b_len=bx2-bx1

        b_h=by2-by1

        area_of_b=b_len*b_h

        #check Overlap

        over_lap_area=max(min(ax2,bx2)-max(bx1,ax1),0) * max(min(ay2,by2)-max(ay1,by1),0)

        reduced_area=(area_of_a+area_of_b)-over_lap_area

        return reduced_area

        

