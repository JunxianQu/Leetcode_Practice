class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        def addRes( state ):
            res = []
            for col in state:
                res.append("".join(col))
            return res
        def backtrack( row, cols, diagonals, anti_diagonals, state ):
            if row == len(state):
                ans.append( addRes( state ) ) 
                return
            for i in range( len( state ) ):
                if i not in cols and i + row not in diagonals and n - i - 1 + row not in anti_diagonals:
                    state[row][i] = 'Q'
                    backtrack( row + 1, cols + [ i ], diagonals + [ i + row ], anti_diagonals + [ n - i - 1 + row ], state )
                    state[row][i] = '.'
        state = [ ['.'] * n for i in range(n) ]
        backtrack( 0, [], [], [], state )            
        return ans