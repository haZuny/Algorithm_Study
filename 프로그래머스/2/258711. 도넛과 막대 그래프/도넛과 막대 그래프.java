/*
정점이 그래프 판별 방법
정점에서 향하는 간선 갯수 > 2 && 정점으로 향하는 간선의 갯수 = 0: 새로 생성한 노드

도넛 그래프 - 모든 노드가 간선(1,1)(새로 생성된 노드가 향하는 노드는 제외)
막대 그래프 - 1개의 노드가 간선(0, 1) OR 노드가 1개 존재 및 간선X
8자 그래프 - 1개의 노드가 간선(2,2), 나머지 노드가 간선(1, 1)
* 간선(out, in)

1. 그래프 맵 생성, 각 간선 당 들어오는 간선 및 나가는 간선 갯수 맵으로 기록
2. 새로 생성된 노드 탐색
3. 새로 생성된 노드 기준 DFS, 탐색시 새로 생성된 노드는 탐색 X
*/

import java.util.*;
class Solution {
    public int[] solution(int[][] edges) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        Map<Integer, int[]> degrees = new HashMap<>();
        Set<Integer> unvisitted = new HashSet<>();
        
        for (int[] edge:edges){
            // 그래프 생성(모든 노드 탐색을 위해 양방향으로)
            try{
                graph.get(edge[0]).add(edge[1]);
            } catch(Exception e){
                List ls = new LinkedList<Integer>();
                ls.add(edge[1]);
                graph.put(edge[0], ls);
            }
            try{
                graph.get(edge[1]).add(edge[0]);
            } catch(Exception e){
                List ls = new LinkedList<Integer>();
                ls.add(edge[0]);
                graph.put(edge[1], ls);
            }
            // 간선 갯수 기록(out, in)
            try{degrees.get(edge[0])[0] += 1;}    // 나가는 노드
            catch(Exception e){
                int[] temp = {1, 0};
                degrees.put(edge[0], temp);
            }
            try{degrees.get(edge[1])[1]++;}    // 들어오는 노드
            catch(Exception e){
                int[] temp = {0, 1};
                degrees.put(edge[1], temp);
            }
            // 방문 여부 위한 set
            unvisitted.add(edge[0]);
            unvisitted.add(edge[1]);
        }
        
        // 새로 생성된 노드 탐색
        int generated=-1;
        for (int node:degrees.keySet()){
            if (degrees.get(node)[0] >= 2 && degrees.get(node)[1] == 0){
                generated = node;
                break;
            }
        }
        
        Stack<Integer> stack = new Stack<Integer>();
        Set visitted = new HashSet();
        visitted.add(generated);
        
        
        int[] answer = {generated, 0, 0, 0};
        
        // 새로 생성된 노드에 연결된 각 그래프를 탐색하며 그래프의 유형 판단
        for (int start:graph.get(generated)){
            // 일정 갯수의 간선을 가지는 노드의 갯수 기록
            int[] edgeNum = {0,0,0,0};   // ( (0, 1), (1, 0), (1, 1), (2, 2) )
            stack.push(start);
            visitted.add(start);
            
            // BFS 탐색
            while(!stack.isEmpty()){
                int node = stack.pop();
                // 새로 생성된 노드가 향하는 노드일 경우 indegree-1
                if (node == start)  degrees.get(node)[1]--;
                // 갯수 기록
                if (degrees.get(node)[0] == 2 && degrees.get(node)[1] == 2)  edgeNum[3]++;
                else if (degrees.get(node)[0] == 1 && degrees.get(node)[1] == 1)    edgeNum[2]++;
                else if (degrees.get(node)[0] == 1 && degrees.get(node)[1] == 0)    edgeNum[1]++;
                else if (degrees.get(node)[0] == 0 && degrees.get(node)[1] == 1)    edgeNum[0]++;
                
                // 연결된 노드 탐색
                try{    // 말단 노드 경우 제외
                    for (int next:graph.get(node)){
                        if (!visitted.contains(next)){
                            stack.push(next);
                            visitted.add(next);
                        }
                    }
                } catch(Exception e){}
            }
            
            // 그래프 유형 판별
            if (edgeNum[3] == 1)    answer[3]++;
            else if (edgeNum[0] == 1 || edgeNum[2] == 0)    answer[2]++;
            else    answer[1]++;
        }
        
        return answer;
    }
}