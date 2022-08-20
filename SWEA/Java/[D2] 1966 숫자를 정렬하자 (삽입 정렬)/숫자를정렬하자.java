import java.util.Arrays;
import java.util.Scanner;

public class 숫자를정렬하자 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		//테스트케이스 개수
		int T = sc.nextInt();
		
		//T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			//숫자 개수
			int N = sc.nextInt();
			int[] num = new int[N];
			
			//N개의 숫자 입력받기
			for (int n = 0; n < N; n++) {
				num[n] = sc.nextInt();
			}
			
			//삽입 정렬
			for (int i = 1; i < num.length; i++) {
				//현재 정렬할 값
				int shift = num[i];
				
				//하나씩 앞으로 가면서 비교 (앞의 숫자보다 작으면 이동)
				int j;	//for문이 끝나고 나서도 j를 써야 하므로 따로 선언
				for (j = i - 1; j >= 0 && shift < num[j]; j--) {
					num[j + 1] = num[j];
				}
				
				//shift값도 이동
				num[j + 1] = shift;
			}
			
			//출력
			System.out.print("#" + t);
			for (int i = 0; i < num.length; i++) {
				System.out.print(" " + num[i]);
			}
			System.out.println();
		}
	}
}
