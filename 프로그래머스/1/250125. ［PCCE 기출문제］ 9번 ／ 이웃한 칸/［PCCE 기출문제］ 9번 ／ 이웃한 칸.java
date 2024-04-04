class Solution {
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        String color = board[h][w];
        int size = board.length;
        
        if(h-1 >= 0 && board[h-1][w].equals(color)){
            answer++;
        }
        if(h+1 <= size-1 && board[h+1][w].equals(color)){
            answer++;
        }
        if(w-1 >= 0 && board[h][w-1].equals(color)){
            answer++;
        }
        if(w+1 <= size-1 && board[h][w+1].equals(color)){
            answer++;
        }
        return answer;
    }
}