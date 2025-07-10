class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < my_string.length(); i++) {
            stringBuilder.append(my_string.charAt(i));
        } 
        
        for (int i = 0; i < overwrite_string.length(); i++) {
            stringBuilder.setCharAt(i + s, overwrite_string.charAt(i));
        }
        
        return stringBuilder.toString();
    }
}