import java.util.*;
import java.io.FileInputStream;

class Solution
{
	 public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);

        for(int test_case = 1; test_case <= 10; test_case++)
        {
            // BackTracking 으로 구현
            // Stack을 사용해서 BT 구현

            int[][] arr = new int[16][16];
            int s_i = 0, s_j = 0;

            // 입력
            sc.nextLine();
            for (int i = 0; i < 16; i++){
                String line = sc.nextLine();
                for (int j = 0; j<16; j++){
                    arr[i][j] = Character.getNumericValue(line.charAt(j));
                    if (arr[i][j] == 2){
                        s_i = i;
                        s_j = j;
                    }
                }
            }

            // Stack에 삽입하는 배열: [탐색할 X, 탐색할 Y]
            Stack<int[]> stack = new Stack<>();
            // 이미 탐색한 노드 Set(i*100 + j)
            Set<Integer> visitted = new HashSet<>();
            visitted.add(s_i*100 + s_j);

            // 첫 노드 삽입
            int[] start = {s_i, s_j};
            stack.push(start);

            int answer = 0;
            boolean run = true;

            // BT 시작
            while(run && !stack.isEmpty()){
                int[] node = stack.pop();
                int i = node[0], j = node[1];

                // 목적지 탐색
                if (i-1>=0 && arr[i-1][j] == 3){
                    answer = 1;
                    run = false;
                }
                if (i+1<=15 && arr[i+1][j] == 3){
                    answer = 1;
                    run = false;
                }
                if (j-1>=0 && arr[i][j-1] == 3){
                    answer = 1;
                    run = false;
                }
                if (j+1<=15 && arr[i][j+1] == 3){
                    answer = 1;
                    run = false;
                }

                // 길 탐색
                int[] temp = {-1,-1};
                if (i-1>=0 && arr[i-1][j] == 0 && !visitted.contains((i-1)*100+j)){
                    temp[0] = i-1;
                    temp[1] = j;
                    stack.push(temp.clone());
                    visitted.add((i-1)*100+j);
                }
                if (i+1<=15 && arr[i+1][j] == 0 && !visitted.contains((i+1)*100+j)){
                    temp[0] = i+1;
                    temp[1] = j;
                    stack.push(temp.clone());
                    visitted.add((i+1)*100+j);
                }
                if (j-1>=0 && arr[i][j-1] == 0 && !visitted.contains(i*100+j-1)){
                    temp[0] = i;
                    temp[1] = j-1;
                    stack.push(temp.clone());
                    visitted.add(i*100+j-1);
                }
                if (j+1<=15 && arr[i][j+1] == 0 && !visitted.contains(i*100+j+1)){
                    temp[0] = i;
                    temp[1] = j+1;
                    stack.push(temp.clone());
                    visitted.add(i*100+j+1);
                }
            }

            System.out.printf("#%d %d\n", test_case, answer);
        }
    }
}