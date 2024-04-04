import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        // 친구들의 수
        int friendsNum = friends.length;
        
        // 이름:인덱스 를 가진 맵 생성
        Map<String,Integer> getFrdIdx = new HashMap();
        for (int i=0; i<friendsNum; i++){
            getFrdIdx.put(friends[i], i);
        }
        
        // 각 친구별 선물 교환 횟수 2차원 리스트[준사람, 받은사람]
        int[][] giftCnt = new int[friendsNum][friendsNum];
        // 선물 지수 리스트
        int[] giftScore = new int[friendsNum];
        
        // gifts 내용 기록
        for (String gift:gifts){
            String[] fromTo = gift.split(" ");
            String from = fromTo[0];
            String to = fromTo[1];
            giftCnt[getFrdIdx.get(from)][getFrdIdx.get(to)]++;
            giftScore[getFrdIdx.get(from)]++;
            giftScore[getFrdIdx.get(to)]--;
        }
        
        int answer = 0;
        
        // 계산
        for (int i = 0; i < friendsNum; i++){
            int cnt = 0;
            for (int j = 0; j < friendsNum; j++){
                if (i != j){
                    // 상대보다 선물 많이 준 경우 카운트
                    if (giftCnt[i][j] > giftCnt[j][i]){
                        cnt++;
                    }
                    // 상대와 같은 경우, 선물 지수 고려
                    else if (giftCnt[i][j] == giftCnt[j][i] && giftScore[i] > giftScore[j]){
                        cnt++;
                    }
                }
            }
            // 가장 높은 점수 갱신
            if (cnt > answer){
                answer = cnt;
            }
        }
        return answer;
    }
}