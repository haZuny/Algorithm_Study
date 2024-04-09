import java.util.*;

class Solution {
    // w >= h
    public int solution(int[][] sizes) {
        int mw = 0, mh = 0;
        
        for (int[] size:sizes){
            int w = Math.max(size[0], size[1]);
            int h = Math.min(size[0], size[1]);
            
            mw = Math.max(mw, w);
            mh = Math.max(mh, h);
        }
        
        int answer = mw * mh;
        return answer;
    }
}