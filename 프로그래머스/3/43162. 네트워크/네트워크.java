import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int size = computers.length;
        
        // BFS로 방문하지 않은 노드 목록
        Set<Integer> unvisit = new HashSet<>();
        for(int i=0; i<size; i++)   unvisit.add(i);
        
        // BFS를 사용하여, 네트워크 단위로 탐색
        Queue<Integer> q = new LinkedList<>();
        Iterator<Integer> iter = unvisit.iterator();
        while(iter.hasNext()){
            answer++;
            int first = iter.next();
            // BFS로 하나의 네트워크 탐색
            q.add(first);
            while(!q.isEmpty()){
                int node = q.remove();
                for (int i=0; i<size; i++){
                    if(computers[node][i] == 1 && unvisit.contains(i))  q.add(i);
                }
                unvisit.remove(node);
                iter = unvisit.iterator();
            }
        }
        
        return answer;
    }
}