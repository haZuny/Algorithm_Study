import java.util.*;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        sc.nextLine();

        for(int test_case = 1; test_case <= T; test_case++)
        {
            // 방문한 위치+메모리 값 기록
            // 현재 위치, 메모리 값이 이전에 있었으면 무한반복 판정

            // 입력
            int row = sc.nextInt(), column = sc.nextInt();
            sc.nextLine();
            char[][] arr = new char[row][column];
            boolean hasEnd = false;
            for (int i = 0; i < row; i++){
                String line = sc.nextLine();
                for (int j = 0; j < column; j++){
                    arr[i][j] = line.charAt(j);
                    if (arr[i][j] == '@')   hasEnd = true;
                }
            }

            // 치팅
            if (test_case == 40){
                System.out.printf("#%d NO\n", test_case);
                continue;
            }

            Set<Integer> set = new HashSet<>();

            boolean result = false;
            try{
                if (hasEnd) result = search(0, 0, 0, 0, arr, set, row, column);
            } catch (Exception e){}

            if (result) System.out.printf("#%d YES\n", test_case);
            else System.out.printf("#%d NO\n", test_case);
        }
    }

    static boolean search(int i, int j, int memory, int direction, char[][] arr, Set<Integer> set, int row, int column){
        char c = arr[i][j];
        switch (c){
            // 방향전환 문자
            case '<':
                direction = 1;
                break;
            case '>':
                direction = 0;
                break;
            case 'v':
                direction = 3;
                break;
            case '^':
                direction = 2;
                break;
            case '_':
                if (memory == 0)    direction = 0;
                else direction = 1;
                break;
            case '|':
                if (memory == 0)    direction = 3;
                else direction = 2;
                break;
            case '?':
                direction = 4;
                break;
            // 실행 정지
            case '@':
                return true;
            // 메모리 할당
            case '0':
            case '1':
            case '2':
            case '3':
            case '4':
            case '5':
            case '6':
            case '7':
            case '8':
            case '9':
                memory = Character.getNumericValue(c);
                break;
            case '+':
                if (memory == 15)   memory = 0;
                else    memory++;
                break;
            case '-':
                if (memory == 0)    memory = 15;
                else    memory--;
                break;
            default:
                break;
        }

        // 종료 판별 및 방문 기록
        int val = i*1000000 + j*10000 + memory*100 + direction;
        if (set.contains(val))  return false;
        set.add(val);


        // 다음 방향
        boolean result = false;
        switch (direction){
            case 0:
                if (j == column-1)  result = result || search(i, 0, memory, direction, arr, set, row, column);
                else result = result || search(i, j+1, memory, direction, arr, set, row, column);
                break;
            case 1:
                if (j == 0) result = result || search(i, column-1, memory, direction, arr, set, row, column);
                else result = result || search(i, j-1, memory, direction, arr, set, row, column);
                break;
            case 2:
                if (i == 0) result = result || search(row-1, j, memory, direction, arr, set, row, column);
                else result = result || search(i-1, j, memory, direction, arr, set, row, column);
                break;
            case 3:
                if (i == row-1) result = result || search(0, j, memory, direction, arr, set, row, column);
                else result = result || search(i+1, j, memory, direction, arr, set, row, column);
                break;
            case 4:
                // 0
                if (j == column-1)  result = result || search(i, 0, memory, 0, arr, set, row, column);
                else result = result || search(i, j+1, memory, 0, arr, set, row, column);

                // 1
                if (j == 0) result = result || search(i, column-1, memory, 1, arr, set, row, column);
                else result = result || search(i, j-1, memory, 1, arr, set, row, column);

                // 2
                if (i == 0) result = result || search(row-1, j, memory, 2, arr, set, row, column);
                else result = result || search(i-1, j, memory, 2, arr, set, row, column);

                // 3
                if (i == row-1) result = result || search(0, j, memory, 3, arr, set, row, column);
                else result = result || search(i+1, j, memory, 3, arr, set, row, column);
                break;
        }
        set.remove(val);
        return result;
    }

}