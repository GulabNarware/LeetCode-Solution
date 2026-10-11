class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        a={}
        rank=1
        for i in sorted(arr):
            if i not in a:
                a[i]=rank
                rank+=1

        result=[0]*len(arr)

        for i in range(len(arr)):
            if arr[i] in a:
                result[i]=a[arr[i]]

        return result

            


