class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_pile=1
        max_pile=max(piles)

        while min_pile<=max_pile:

            mid=(min_pile+max_pile)//2
            hourse=0
            for pile in piles:
                hourse+=ceil(pile/mid)

            if hourse<=h:
                max_pile=mid-1

            else:
                min_pile=mid+1

        return min_pile

