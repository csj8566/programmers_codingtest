class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();
        
        sb1.append(String.valueOf(a));
        sb1.append(String.valueOf(b));
        
        sb2.append(String.valueOf(b));
        sb2.append(String.valueOf(a));
        
        String string1 = sb1.toString();
        String string2 = sb2.toString();
        
        int int1 = Integer.valueOf(string1);
        int int2 = Integer.valueOf(string2);
        
        if (int1 >= int2) {
            return int1;
        } else {
            return int2;
        }
    }
}