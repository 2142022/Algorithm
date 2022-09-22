import java.util.Scanner;

public class 거듭제곱 {

	// N의 M제곱 구하기
	static int N;
	static int M;

	static int ans;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 10개의 테스트케이스
		for (int t = 1; t <= 10; t++) {
			// 테스트케이스 번호
			t = sc.nextInt();

			// N의 M제곱 구하기
			N = sc.nextInt();
			M = sc.nextInt();
			
			// 0승은 무조건 1
			if (M == 0) {
				ans = 1;
			} 
			// 0이나 1이면 무조건 0이나 1
			else if (N == 0 || N == 1) {
				ans = N;
			} 
			// 그 외에는 재귀로 구하기
			else {
				power(1, 1);
			}

			System.out.printf("#%d %d\n", t, ans);
		}
	}

	private static void power(int i, int result) {
		// M번 재귀하면 결과값 저장하고 끝내기
		if (i == M + 1) {
			ans = result;
			return;
		}

		power(i + 1, result * N);
	}
}
