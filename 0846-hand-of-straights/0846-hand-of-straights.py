class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        hand.sort()
        h={}
        indx=0
        arr=[]
        h_indx=0
        while indx<len(hand):

            if len(arr)==0:
                arr.append(hand[indx])
                hand.pop(indx)

            else:
                if hand[indx]-arr[-1]==1:
                    arr.append(hand[indx])
                    hand.pop(indx)

                elif hand[indx]-arr[-1]==0:
                    indx+=1

                else:
                    return False

            if len(arr)==groupSize:
                h[h_indx]=arr

                arr=[]
                indx=0
                h_indx+=1

        if len(arr)<groupSize and len(arr)!=0:
            return False

        return True

        


            

            

            

