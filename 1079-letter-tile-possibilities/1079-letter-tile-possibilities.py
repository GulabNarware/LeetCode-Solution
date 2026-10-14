class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        c=0
        nums=sorted(tiles)
        def back(indx,nums):
            nonlocal c
            c+=1
            used=set()
            for i in range(indx,len(tiles)):
                if nums[i] in used:
                    continue

                used.add(nums[i])

                nums[i],nums[indx]=nums[indx],nums[i]

                back(indx+1,nums)

                nums[i],nums[indx]=nums[indx],nums[i]

                

        back(0,nums)
        return c-1

