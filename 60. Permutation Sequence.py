class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        product = [ 1 for i in range(n) ]
        nums = [ i for i in range(1, n+1) ]
        for i in range( n-1, 0, -1 ):
            product[i-1] = product[i] * (n-i)
        for i in range(0, n):
            tmp = math.ceil( k/product[i] )
            res.append( nums.pop( tmp-1 ) )
            k = k - (tmp - 1) * product[i] 
        ans = [ str(i) for i in res ]
        return ''.join(ans)