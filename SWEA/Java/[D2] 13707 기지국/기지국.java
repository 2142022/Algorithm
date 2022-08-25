import java.util.Scanner;

public class 기지국 {
	// 배열의 크기
	static int n;

	// nxn 배열
	static char[][] map;

	// 아무것도 없거나 기지국이 체크할 수 있으면 1, 아니면 0
	static int[][] flag;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 배열의 크기
			n = sc.nextInt();

			// nxn 배열
			map = new char[n][n];
			for (int i = 0; i < n; i++) {
				String tmp = sc.next();
				for (int j = 0; j < n; j++) {
					map[i][j] = tmp.charAt(j);
				}
			}

			// 아무것도 없거나 기지국이 체크할 수 있으면 1, 아니면 0
			flag = new int[n][n];

			// 아무것도 없는 곳 체크
			check('X', 0);

			// 기지국 A가 커버하는 곳 체크
			check('A', 1);

			// 기지국 B가 커버하는 곳 체크
			check('B', 2);

			// 기지국 C가 커버하는 곳 체크
			check('C', 3);

			// flag가 0인 곳 개수 확인
			int cnt = 0;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (flag[i][j] == 0) {
						cnt++;
					}
				}
			}

			System.out.printf("#%d %d\n", t, cnt);
		}
	}

	// 문자 c가 있는 상하좌우 d만큼 1체크
	static private void check(char c, int d) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (map[i][j] == c) {
					for (int k = 0; k <= d; k++) {
						// 상
						if (i - k >= 0) {
							flag[i - k][j] = 1;
						}

						// 하
						if (i + k < n) {
							flag[i + k][j] = 1;
						}

						// 좌
						if (j - k >= 0) {
							flag[i][j - k] = 1;
						}

						// 우
						if (j + k < n) {
							flag[i][j + k] = 1;
						}
					}
				}
			}
		}
	}
}