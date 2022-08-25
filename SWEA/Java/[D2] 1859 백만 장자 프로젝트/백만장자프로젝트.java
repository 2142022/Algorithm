import java.util.Scanner;

public class 백만장자프로젝트 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 연속된 날짜 수
			int N = sc.nextInt();

			// 각 날의 매매가
			int[] price = new int[N];

			for (int i = 0; i < N; i++) {
				price[i] = sc.nextInt();
			}

			// 이익
			long plus = 0;

			// 현재 최대 매매가
			int max = price[N - 1];

			// 뒤에서부터 값을 비교
			// 현재 최대 매매가보다 값이 작으면 지출, 값이 크거나 같으면 지금까지의 이익을 구하고 max값 변경
			for (int i = N - 2; i >= 0; i--) {
				// 현재 최대 매매가보다 작을 때
				if (price[i] < max) {
					plus = plus - price[i] + max;
				}

				// 현재 최대 매매가보다 크거나 같을 때
				else {
					max = price[i];
				}
			}

			// 출력
			System.out.printf("#%d %d\n", t, plus);
		}
	}
}