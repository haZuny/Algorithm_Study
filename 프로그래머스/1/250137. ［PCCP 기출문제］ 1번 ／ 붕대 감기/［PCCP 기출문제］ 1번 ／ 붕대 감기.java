class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        
    int chargeTime = bandage[0];
    int healPerSec = bandage[1];
    int healCharge = bandage[2];
    
    int answer = health;
    int lastTime = 0;
        
    for (int[] attack:attacks){
        int time = attack[0] - lastTime;    // 마지막 공격으로 부터의 시간
        int damage = attack[1];
        
        // 1초마다 회복
        answer += healPerSec * (time-1); 
        // 붕대감기 성공
        answer += (time/chargeTime) * healCharge;
        // 붕대감기 끝나는 타이밍에 공격 받는 경우
        if (time/chargeTime >= 1 && time%chargeTime == 0){
            answer -= healCharge;
        }
        // 최대 체력 반영
        if (answer > health){
            answer = health;
        }
        // 몬스터 공격
        answer -= damage;
        // 케릭터 죽을 경우
        if (answer <= 0){
            answer = -1;
            break;
        }
        // 마지막 시간 기록
        lastTime = attack[0];
    }
    return answer;
    }
}