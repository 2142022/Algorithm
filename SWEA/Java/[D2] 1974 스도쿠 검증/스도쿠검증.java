import java.util.Scanner;

public class 스도쿠검증 {
	// 스도쿠 숫자
	static int[][] map;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 스도쿠 숫자 입력받기
			map = new int[9][9];
			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 9; j++) {
					map[i][j] = sc.nextInt();
				}
			}

			// 스도쿠가 올바르게 채워졌으면 1, 아니면 0
			int flag = 1;

			// 가로, 세로 확인
			if (!rowCheck() || !colCheck()) {
				flag = 0;
			}

			// 3X3 격자 확인
			else {
				for (int i = 0; i < 9; i += 3) {
					for (int j = 0; j < 9; j += 3) {
						if (!squareCheck(i, j)) {
							flag = 0;
						}
					}
				}
			}

			System.out.printf("#%d %d\n", t, flag);
		}
	}

	// 가로 확인
	static boolean rowCheck() {
		for (int i = 0; i < 9; i++) {
			// 숫자가 사용되면 cnt++
			int[] cnt = new int[9];
			for (int j = 0; j < 9; j++) {
				cnt[map[i][j] - 1]++;
			}

			// 숫자가 한번씩 사용되었는지 확인
			for (int j = 0; j < 9; j++) {
				if (cnt[j] != 1) {
					return false;
				}
			}
		}

		return true;
	}

	// 세로 확인
	static boolean colCheck() {
		for (int i = 0; i < 9; i++) {
			// 숫자가 사용되면 cnt++
			int[] cnt = new int[9];
			for (int j = 0; j < 9; j++) {
				cnt[map[j][i] - 1]++;
			}

			// 숫자가 한번씩 사용되었는지 확인
			for (int j = 0; j < 9; j++) {
				if (cnt[j] != 1) {
					return false;
				}
			}
		}

		return true;
	}

	// 3X3 격자 확인
	static boolean squareCheck(int r, int c) {
		// 숫자가 사용되면 cnt++
		int[] cnt = new int[9];

		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				cnt[map[r + i][c + j] - 1]++;
			}
		}

		for (int i = 0; i < 9; i++) {
			if (cnt[i] != 1) {
				return false;
			}
		}

		return true;
	}
}
