class Solution:
    def minTotalDistance(self, grid):
        row_sum = []
        col_sum = []
        for i in range( len( grid ) ):
            tmp = 0
            for j in range( len( grid[0] ) ):
                tmp += grid[i][j]
            row_sum.append( tmp )
        for j in range( len( grid[0] ) ):
            tmp = 0
            for i in range( len( grid ) ):
                tmp += grid[i][j]
            col_sum.append( tmp )
        def minTotalDistance1D(vec):
            i, j = -1, len(vec)
            d = left = right = 0
            while i != j:
                if left < right:
                    d += left
                    i += 1
                    left += vec[i]
                else:
                    d += right
                    j -= 1
                    right += vec[j]
            return d

        return minTotalDistance1D(row_sum) + minTotalDistance1D(col_sum)