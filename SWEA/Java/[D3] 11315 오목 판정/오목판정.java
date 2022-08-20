import java.util.Scanner;

public class 오목판정 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 판의 크기
			int N = sc.nextInt();

			// 판 입력받기 (돌이 있으면 1, 없으면 0)
			int[][] map = new int[N][N];

			for (int i = 0; i < N; i++) {
				char[] tmp = sc.next().toCharArray();

				// 1과 0으로 변환하기
				for (int j = 0; j < N; j++) {
					if (tmp[j] == '.') {
						map[i][j] = 0;
					} else {
						map[i][j] = 1;
					}
				}
			}

			// 가로 체크
			if (check_row(map, N)) {
				System.out.printf("#%d YES\n", t);
				continue;
			}

			// 세로 체크
			if (check_col(map, N)) {
				System.out.printf("#%d YES\n", t);
				continue;
			}

			// 대각선 체크 (\ 방향)
			if (check_diag1(map, N)) {
				System.out.printf("#%d YES\n", t);
				continue;
			}

			// 대각선 체크 (/ 방향)
			if (check_diag2(map, N)) {
				System.out.printf("#%d YES\n", t);
				continue;
			}

			System.out.printf("#%d NO\n", t);
		}
	}

	// 가로 체크
	static boolean check_row(int[][] map, int N) {
		for (int i = 0; i < N; i++) {
			// 연속하는 1의 개수
			int cnt = 0;

			for (int j = 0; j < N; j++) {
				if (map[i][j] == 1) {
					cnt++;
				} else {
					cnt = 0;
				}

				if (cnt == 5) {
					return true;
				}
			}
		}

		return false;
	}

	// 세로 체크
	static boolean check_col(int[][] map, int N) {
		for (int j = 0; j < N; j++) {
			// 연속하는 1의 개수
			int cnt = 0;

			for (int i = 0; i < N; i++) {
				if (map[i][j] == 1) {
					cnt++;
				} else {
					cnt = 0;
				}

				if (cnt == 5) {
					return true;
				}
			}
		}

		return false;
	}

	// 대각선 체크 (\ 방향)
	static boolean check_diag1(int[][] map, int N) {
		for (int n = 0; n <= N - 5; n++) {
			// 연속하는 1의 개수
			int cnt = 0;

			for (int i = 0, j = 0; j + n < N; i++, j++) {
				if (map[i][j + n] == 1) {
					cnt++;
				} else {
					cnt = 0;
				}

				if (cnt == 5) {
					return true;
				}
			}

			cnt = 0;

			for (int i = 1, j = 0; i + n < N; i++, j++) {
				if (map[i + n][j] == 1) {
					cnt++;
				} else {
					cnt = 0;
				}

				if (cnt == 5) {
					return true;
				}
			}
		}

		return false;
	}

	// 대각선 체크 (/ 방향)
	static boolean check_diag2(int[][] map, int N) {
		for (int n = 0; n <= N - 5; n++) {
			// 연속하는 1의 개수
			int cnt = 0;

			for (int i = 0, j = N - 1; j - n >= 0; i++, j--) {
				if (map[i][j - n] == 1) {
					cnt++;
				} else {
					cnt = 0;
				}

				if (cnt == 5) {
					return true;
				}
			}

			cnt = 0;

			for (int i = 1, j = N - 1; i + n < N; i++, j--) {
				if (map[i + n][j] == 1) {
					cnt++;
				} else {
					cnt = 0;
				}

				if (cnt == 5) {
					return true;
				}
			}
		}

		return false;
	}
}
