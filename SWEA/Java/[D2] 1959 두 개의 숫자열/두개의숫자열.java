import java.util.Scanner;

public class 두개의숫자열 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 두 개의 숫자열의 숫자 개수
			int N = sc.nextInt();
			int M = sc.nextInt();

			// 숫자열 입력받기
			int[] arrN = new int[N];
			int[] arrM = new int[M];

			for (int i = 0; i < N; i++) {
				arrN[i] = sc.nextInt();
			}

			for (int i = 0; i < M; i++) {
				arrM[i] = sc.nextInt();
			}

			// 최대값
			int max = -2147483648;
			for (int i = 0; i < Math.abs(N - M) + 1; i++) {
				// arrN[i] X arrM[i]
				int tmp = 0;

				for (int j = 0; j < Math.min(N, M); j++) {
					if (N <= M) {
						tmp = tmp + arrN[j] * arrM[i + j];
					} else {
						tmp = tmp + arrN[i + j] * arrM[j];
					}
				}

				max = Math.max(max, tmp);
			}

			// 출력
			System.out.printf("#%d %d\n", t, max);
		}
	}
}
