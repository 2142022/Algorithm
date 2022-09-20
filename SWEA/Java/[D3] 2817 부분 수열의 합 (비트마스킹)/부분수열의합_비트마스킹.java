import java.util.Scanner;

public class 부분수열의합_비트마스킹 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 자연수 개수
			int N = sc.nextInt();

			// N개의 자연수의 합
			int K = sc.nextInt();

			// N개의 자연수
			int[] A = new int[N];
			for (int i = 0; i < N; i++) {
				A[i] = sc.nextInt();
			}

			// 합이 K가 되는 경우의 수
			int cnt = 0;

			// 비트마스킹으로 1개 이상의 원소 선택
			for (int i = 0; i < (1 << N); i++) {
				// 선택한 자연수의 합
				int sum = 0;

				for (int j = 0; j < N; j++) {
					if ((i & (1 << j)) > 0) {
						sum += A[j];
					}
				}

				// 합이 K가 되면 cnt++
				if (sum == K) {
					cnt++;
				}
			}

			System.out.printf("#%d %d\n", t, cnt);
		}
	}
}
