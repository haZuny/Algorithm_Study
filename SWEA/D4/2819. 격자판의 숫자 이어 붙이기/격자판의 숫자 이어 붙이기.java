import java.util.*;

public class Solution {
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
        {
            int[][] arr = new int[4][4];
            for (int i = 0; i < 4; i++){
                for (int j = 0; j < 4; j++){
                    arr[i][j] = sc.nextInt();
                }
            }

            // [pos, cnt, num], pos: i*100 + j
            Queue<int[]> queue = new LinkedList<int[]>();
            Set<Integer> set = new HashSet<Integer>();

            // 첫 노드 삽입
            for (int i = 0; i < 4; i++){
                for (int j = 0; j < 4; j++){
                    int[] node = {i*100+j, 1, arr[i][j]};
                    queue.add(node);
                }
            }

            // BFS 탐색
            while (!queue.isEmpty()){
                int[] node = queue.remove();
                // 7자리 수 완성 된 경우
                if (node[1] >= 7){
                    set.add(node[2]);
                }
                // 상하좌우 탐색
                else{
                    int i = node[0]/100;
                    int j = node[0]%100;

                    try{
                        int nextVal = node[2]*10 + arr[i-1][j];
                        int[] nextNode = {(i-1)*100+j, node[1]+1, nextVal};
                        queue.add(nextNode);
                    } catch (Exception e){}
                    try{
                        int nextVal = node[2]*10 + arr[i+1][j];
                        int[] nextNode = {(i+1)*100+j, node[1]+1, nextVal};
                        queue.add(nextNode);
                    } catch (Exception e){}
                    try{
                        int nextVal = node[2]*10 + arr[i][j-1];
                        int[] nextNode = {i*100+j-1, node[1]+1, nextVal};
                        queue.add(nextNode);
                    } catch (Exception e){}
                    try{
                        int nextVal = node[2]*10 + arr[i][j+1];
                        int[] nextNode = {i*100+j+1, node[1]+1, nextVal};
                        queue.add(nextNode);
                    } catch (Exception e){}
                }
            }

            System.out.printf("#%d %d\n", test_case, set.size());
        }
    }
}