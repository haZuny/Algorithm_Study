import java.util.*;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);

        for(int test_case = 1; test_case <= 10; test_case++)
        {
            int n = sc.nextInt();
            int start = sc.nextInt();
            Map<Integer, List<Integer>> graph = new HashMap<>();
            for (int i = 0; i < n/2; i++){
                int from = sc.nextInt();
                int to = sc.nextInt();
                try{
                    List<Integer> ls = graph.get(from);
                    if (!ls.contains(to))  ls.add(to);
                }catch (Exception e){
                    List<Integer> ls = new ArrayList<>();
                    ls.add(to);
                    graph.put(from, ls);
                }
            }

            // int[]: [node, 방문되는 순서]
            Queue<int[]> queue = new LinkedList<>();
            Set<Integer> visitted = new HashSet<>();

            // 첫 노드 삽입
            int[] startNode = {start, 0};
            queue.add(startNode);
            visitted.add(start);

            // 정답 기록
            int latest = -1;
            int biggest = 0;

            // BFS
            while (!queue.isEmpty()){
                int[] node = queue.remove();

                // 정답 업데이트
                if (latest < node[1]){
                    latest = node[1];
                    biggest = 0;
                }
                if (latest == node[1] && biggest < node[0]){
                    biggest = node[0];
                }


                // 연결된 노드 없으면 Pass
                if (!graph.keySet().contains(node[0]))  continue;

                // 탐색
                int[] temp = {-1, node[1]+1};
                for (int next:graph.get(node[0])){
                    temp[0] = next;
                    if (!visitted.contains(next)){
                        queue.add(temp.clone());
                        visitted.add(next);
                    }
                }
            }

            System.out.printf("#%d %d\n", test_case, biggest);
        }
    }
}