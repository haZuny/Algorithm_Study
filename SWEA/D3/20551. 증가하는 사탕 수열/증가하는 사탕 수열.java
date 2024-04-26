import java.util.*;

public class Solution {
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
        {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();

            // 만들 수 없는 경우
            if (b < 2 || c < 3) System.out.printf("#%d -1\n", test_case);

            // 사탕 없애기
            else{
                int min_b = 0;
                int min_a = 0;

                if (b >= c){
                    min_b = b-c+1;
                    b = c-1;
                }

                if (a >= b){
                    min_a = a-b+1;
                    a = b-1;
                }
                System.out.printf("#%d %d\n", test_case, min_b + min_a);
            }

        }
    }
}