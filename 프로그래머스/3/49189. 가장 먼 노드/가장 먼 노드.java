import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        int distance = 0;
        int cnt = 0;
        
        // 그래프 생성
        Map<Integer, ArrayList<Integer>> graph = new HashMap<>();
        for (int[] nodes:edge){
            // s->e
            try{
                graph.get(nodes[0]).add(nodes[1]);
            } catch (Exception e){
                graph.put(nodes[0], new ArrayList<Integer>());
                graph.get(nodes[0]).add(nodes[1]);
            }
            // e->s
            try{
                graph.get(nodes[1]).add(nodes[0]);
            } catch (Exception e){
                graph.put(nodes[1], new ArrayList<Integer>());
                graph.get(nodes[1]).add(nodes[0]);
            }
        }
        
        // 그래프 탐색(BFS) 준비
        Set<Integer> visited = new HashSet<>(); // 방문한 노드 기록
        visited.add(1);
        Queue<int[]> q = new LinkedList<int[]>();
        int[] first = {1, 0};   // [node, distance]
        q.add(first);
        
        // BFS 탐색
        while (!q.isEmpty()){
            int[] node = q.remove();
            // 최대 거리와 개수 업데이트
            if (node[1] == distance)    cnt++;
            else if(node[1] > distance){
                distance = node[1];
                cnt = 1;
            }
            // 연결된 노드 탐색
            int[] temp = {0, node[1]+1};
            for (int next:graph.get(node[0])){
                if(graph.containsKey(next) && !visited.contains(next)){
                    temp[0] = next;
                    q.add(temp.clone());
                    visited.add(next);
                }
            }
        }
        
        return cnt;
    }
}