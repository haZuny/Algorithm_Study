import java.io.*;
import java.math.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int num = Integer.parseInt(br.readLine()); //n 입력
    BigInteger n = new BigInteger("2"); //2의 n제곱이 매우 커질 수도 있기 때문에 BigInteger사용
    BigInteger k = n.pow(num).subtract(BigInteger.ONE); //이동횟수 계산
    System.out.println(k); //이동횟수 우선 출력

    //n이 20 이하인 경우에만 재귀함수 호출
    if(num < 21) {
      hanoi(num, 1, 2, 3);
    }
  }

  //원판 개수, 시작점, 중간점, 끝점
  public static void hanoi(int num, int s, int m, int e) {
    if(num == 1) {
      System.out.println(s + " " + e);
    }
    else {
      hanoi(num-1, s, e, m); //n-1호출시 중간으로 이동하는 것이기 때문에 바꿔서 호출
      System.out.println(s + " " + e); //이동내용 출력
      hanoi(num-1, m, s, e); //중간으로 옮긴 것을 마지막으로 옮겨주어야 하기 때문에 바꿔서 호출
    }
  }
}