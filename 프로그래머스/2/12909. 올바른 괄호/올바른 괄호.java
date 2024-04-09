import java.util.*;

class Solution {
    boolean solution(String s) {
        Stack stack = new Stack();

        for(char c:s.toCharArray()){
            // '(': 0, ')':1
            try{
                if (c == '(')   stack.push(0);
                else stack.pop();
            }
            // 스택에서 null에러가 나면 false
            catch (Exception e){
                return false;
            }
        }
        
        // 스택이 비어있으면 true, 괄호가 남으면 false
        if (stack.size() == 0)  return true;
        else return false;
    }
}