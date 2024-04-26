import java.util.*;
import java.io.FileInputStream;
/*
dp 방식으로 해결
*/
class Solution
{
	public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
        {
            int size = sc.nextInt();
            // 배열 입력 받기
            sc.nextLine();	// reset buf
            int[][] arr = new int[size][size];	// 입력받은 지도 배열
            for (int i = 0; i < size; i++){
                String row = sc.nextLine();
                for (int j = 0; j < size; j++){
                    arr[i][j] = Character.getNumericValue(row.charAt(j));
                }
            }

            int[][] dp = new int[size][size];
            for (int i=0; i<size; i++){
                for (int j = 0; j <size; j++){
                    dp[i][j] = Integer.MAX_VALUE;
                }
            }
            dp[0][0] = arr[0][0];

            // dp 배열 갱신하면서 탐색
            boolean changeDetect;
            do {
                changeDetect = false;
                for (int i = 0; i < size; i++){
                    for (int j = 0; j < size; j++) {
                        if (i==0 && j==0)   continue;
                        int val1 = Integer.MAX_VALUE;
                        int val2 = Integer.MAX_VALUE;
                        int val3 = Integer.MAX_VALUE;
                        int val4 = Integer.MAX_VALUE;
                        try {val1 = dp[i-1][j];} catch (Exception e){};
                        try {val2 = dp[i+1][j];} catch (Exception e){};
                        try {val3 = dp[i][j-1];} catch (Exception e){};
                        try {val4 = dp[i][j+1];} catch (Exception e){};
                        int temp = dp[i][j];
                        dp[i][j] = arr[i][j] + Math.min(val1, Math.min(val2, Math.min(val3, val4)));
                        if (temp != dp[i][j])   changeDetect = true;
                    }
                }
            }while(changeDetect);

            System.out.printf("#%d %d\n", test_case, dp[size-1][size-1]);
        }
    }
}