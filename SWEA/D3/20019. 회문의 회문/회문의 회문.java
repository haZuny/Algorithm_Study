import java.util.Scanner;
import java.io.FileInputStream;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
        sc.nextLine();	// 버퍼 비우기

		for(int test_case = 1; test_case <= T; test_case++)
		{
			String s = sc.nextLine();
            
            boolean check = check(s);
            if (check == false){
            	System.out.printf("#%d NO\n", test_case);
                continue;
            }
            // 짝수
            if (s.length()%2 == 0){
                check = check(s.substring(0, s.length()/2));
                if (check == false){
            	System.out.printf("#%d NO\n", test_case);
                continue;
            }
                check = check(s.substring(s.length()/2, s.length()));
                if (check == false){
            	System.out.printf("#%d NO\n", test_case);
                continue;
            }
            }
            // 홀수
            else{
            	check = check(s.substring(0, s.length()/2));
                if (check == false){
            	System.out.printf("#%d NO\n", test_case);
                continue;
            }
                check = check(s.substring(s.length()/2+1, s.length()));
                if (check == false){
            	System.out.printf("#%d NO\n", test_case);
                continue;
            }
            }
            
            System.out.printf("#%d YES\n", test_case);

		}
	}
    
    static boolean check(String s){
    	int len = s.length();
            int l = 0;
            int r = len-1;
            boolean check = true;
            while (r > l){
            	char lc = s.charAt(l++);
                char rc = s.charAt(r--);
                if (lc != rc)	{
                	check = false;
                    break;
                }
            }
        return check;
    }
}