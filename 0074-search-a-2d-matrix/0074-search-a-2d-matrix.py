class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        main_left=0
        main_right=len(matrix)-1

        while main_left<=main_right:
            mid=(main_left+main_right)//2

            if matrix[mid][0]<=target and matrix[mid][len(matrix[mid])-1]>=target:
                left=0
                right=len(matrix[mid])-1

                while left<=right:

                    sec_mid=(left+right)//2

                    if matrix[mid][sec_mid]==target:
                        return True

                    elif matrix[mid][sec_mid]>target:
                        right=sec_mid-1

                    else:
                        left=sec_mid+1

                return False

            elif matrix[mid][0]>target:
                main_right=mid-1
            else:
                main_left=mid+1
        return False