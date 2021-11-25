class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack( row, cols, diagonals, anti_diagonals, n ):
            if row == n:
                return 1
            ans = 0
            for i in range( n ):
                if i not in cols and i + row not in diagonals and n - i - 1 + row not in anti_diagonals:
                    ans += backtrack( row + 1, cols + [ i ], diagonals + [ i + row ], anti_diagonals + [ n - i - 1 + row ], n )
            return ans
        return backtrack( 0, [], [], [], n)            
        