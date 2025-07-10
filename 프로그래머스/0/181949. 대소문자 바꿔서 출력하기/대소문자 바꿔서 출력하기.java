import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        // 대문자인지 소문자인지 체크하는 로직 필요
        // 만약 대문자면 소문자로
        // 만약 소문자면 대문자로
        
        StringBuilder result = new StringBuilder();
        
        // 문자열 길이만큼 for 문 돌기
        for (int i = 0; i < a.length(); i++){
            // 대소문자 체크
            if (Character.isUpperCase(a.charAt(i))){
                result.append(Character.toLowerCase(a.charAt(i)));
            } else {
                result.append(Character.toUpperCase(a.charAt(i)));
            }
        }
        
        System.out.println(result.toString());
    }
}