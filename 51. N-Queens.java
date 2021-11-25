class Solution {
    Set<Integer> colSet;
    Set<Integer> leftlineSet;
    Set<Integer> rightlineSet;
    List<List<String>> result;
    public List<List<String>> solveNQueens(int n) {
        colSet = new HashSet();
        leftlineSet = new HashSet();
        rightlineSet = new HashSet();
        result = new ArrayList();
        for ( int i = 0; i < n; i++ ) {
            colSet.add( i );
        }
        for ( int i = 0; i < 2*n -1; i++ ) {
            leftlineSet.add( i );
            rightlineSet.add( i );
        }
        recursiveNQueens(n, 0, new ArrayList<Integer>());
        return result;
    }
    public void recursiveNQueens( int n, int index, List<Integer> arr ) {
        if ( index == n ) {
            addResults( arr, n );
            return;
        }
        if ( colSet.isEmpty() || leftlineSet.isEmpty() || rightlineSet.isEmpty() ) return;
        for ( int i = 0; i < n; i++ ) {
            if ( colSet.contains( i ) && leftlineSet.contains( i + index ) && rightlineSet.contains( n-i-1 + index )) {
                colSet.remove( i );
                leftlineSet.remove( i + index );
                rightlineSet.remove( n-i-1 + index );
                arr.add( i );
                recursiveNQueens( n, index + 1, arr );
                arr.remove( arr.size() - 1 );
                colSet.add( i );
                leftlineSet.add( i + index );
                rightlineSet.add( n-i-1 + index );
            }
        }
    }
    public void addResults( List<Integer> arr, int n ) {
        List<String> currentRes = new ArrayList();
        for ( int col : arr ) {
            String tmp = "";
            for ( int i = 0; i < n; i++ ) {
                if ( col == i ) {
                    tmp += "Q";
                } else {
                    tmp += ".";
                }
            }
            currentRes.add( tmp );
        }
        result.add( currentRes );
    }
}