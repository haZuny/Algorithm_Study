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
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

            // 각 건물에 대해 좌 우 2칸씩 중에서 가장 높은 층 파악 후, 해당 건물의 조망 확보 층 계산
            int answer = 0;
            for (int i = 0; i < n; i++){
                int nearbyHeight = 0;
                if (i-2 >= 0 && nearbyHeight < arr[i-2])    nearbyHeight = arr[i-2];
                if (i-1 >= 0 && nearbyHeight < arr[i-1])    nearbyHeight = arr[i-1];
                if (i+1 <= n-1 && nearbyHeight < arr[i+1])    nearbyHeight = arr[i+1];
                if (i+2 <= n-1 && nearbyHeight < arr[i+2])    nearbyHeight = arr[i+2];

                answer += Math.max(arr[i] - nearbyHeight, 0);
            }

            System.out.printf("#%d %d\n", test_case, answer);
        }
    }
}