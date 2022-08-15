import java.util.Scanner;
 
class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
         
        //테스트케이스 입력받고 실행
        int T = sc.nextInt();
        for (int t = 1; t <= T; t++) {
            // 단어 입력받기
            String word = sc.next();
             
            // 배열로 바꾸기
            char[] tmp = word.toCharArray();
             
            //회문이면 1, 아니면 0
            int flag = 1;
             
            //회문검사
            for (int i = 0; i < tmp.length / 2; i++) {
                if (tmp[i] != tmp[tmp.length - i - 1]) {
                    flag = 0;
                    break;
                }
            }
             
            System.out.printf("#%d %d\n", t, flag);
        }
    }
}