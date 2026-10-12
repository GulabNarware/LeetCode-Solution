class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        Row,Col=len(board),len(board[0])
        track=set()

        def dfs(r,c,i):

            if i==len(word):
                return True

            if (r<0 or c<0 or r>=Row or c>=Col):
                return False

            if (word[i]!=board[r][c] or (r,c) in track):
                return False

            track.add((r ,c))

            res=(dfs(r,c+1,i+1) or 
                dfs(r,c-1,i+1)or
                dfs(r+1,c,i+1)or
                dfs(r-1,c,i+1))
            track.remove((r,c))
            return res

        for r in range(len(board)) :
            for c in range(len(board[0])):
                if dfs(r,c,0): return True

        return False