import java.util.Scanner;

public class 연속된1의개수중최대값구하기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 수열의 길이
			int N = sc.nextInt();

			// 수열
			int[] num = new int[N];
			String tmp = sc.next();
			for (int i = 0; i < N; i++) {
				num[i] = tmp.charAt(i) - '0';
			}

			// 연속된 1의 개수 중 최대값
			int max = 0;
			for (int i = 0; i < N; i++) {
				// 연속된 1의 개수
				int cnt = 0;

				while (i < N && num[i] == 1) {
					i++;
					cnt++;
				}

				// max값과 비교
				max = Math.max(cnt, max);
			}

			// 출력
			System.out.printf("#%d %d\n", t, max);
		}
	}
}