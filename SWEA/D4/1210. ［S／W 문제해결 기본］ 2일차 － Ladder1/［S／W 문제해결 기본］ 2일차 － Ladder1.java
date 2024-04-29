/*
X에서부터 역으로 검사
*/
import java.util.*;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        sc.nextInt();

        // 입력
        for(int test_case = 1; test_case <= 10; test_case++)
        {
            int[][] arr = new int[100][100];
            int dest = 0;
            for (int i = 0; i < 100; i++){
                for (int j = 0; j < 100; j++){
                    arr[i][j] = sc.nextInt();
                    // 도착지 검색
                    if (i == 99 && arr[i][j] == 2)	dest = j;
                }
            }

            int i = 100;
            int j = dest;

            // direction: 검사하던 방향
            // 0: i-1
            // 1: j-1
            // 2: j+1
            int direction = 0;
            // 목적지에서 부터 탐색
            while (i >= 0){
                // 위로 이동 중
                if (direction == 0){
                    // 양 옆으로 빠질 수 있으면 빠짐
                    if (i <= 99 && j-1 >= 0 && arr[i][j-1] == 1){
                        j--;
                        direction = 1;
                    }
                    else if (i <= 99 && j+1 <= 99 && arr[i][j+1] == 1){
                        j++;
                        direction = 2;
                    }
                    // 옆에 길이 없으면 계속 올라감
                    else	i--;
                }
                // 왼쪽으로 이동 중
                else if (direction == 1){
                    // 왼쪽으로 길이 있으면 계속 이동
                    if (j-1 >= 0 && arr[i][j-1] == 1)	j--;
                        // 길이 없으면 위로 올라감
                    else{
                        i--;
                        direction = 0;
                    }
                }
                // 오른 쪽으로 이동 중
                else if (direction == 2){
                    // 오른쪽으로 길이 있으면 계속 이동
                    if (j+1 <= 99 && arr[i][j+1] == 1)	j++;
                        // 길이 없으면 위로 올라감
                    else{
                        i--;
                        direction = 0;
                    }
                }
            }

            System.out.printf("#%d %d\n", test_case, j);
            
            try{sc.nextInt();}catch(Exception e){}}
    }
}