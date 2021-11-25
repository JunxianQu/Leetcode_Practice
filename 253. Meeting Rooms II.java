class Solution {
    public int minMeetingRooms(int[][] intervals) {
        Arrays.sort( intervals, new Comparator<int[]>(){
           public int compare( int[] o1, int[] o2) {
               return o1[0] - o2[0];
           }
        });
        PriorityQueue<Integer> result = new PriorityQueue();
        for ( int[] interval : intervals ) {
            if ( result.size() == 0 ) {
                result.add( interval[1] );
            } else if( result.peek() <= interval[0] ) {
                result.poll();
                result.add( interval[1] );
            } else {
                result.add( interval[1] );
            }
        }
        return result.size();
    }
}