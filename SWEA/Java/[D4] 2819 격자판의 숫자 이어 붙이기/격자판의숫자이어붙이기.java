import java.util.HashSet;
import java.util.Scanner;

public class 격자판의숫자이어붙이기 {

	// 일곱 자리 수들을 나타내는 Set
	static HashSet<String> set;

	// 4X4 격자판
	static int[][] map;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 일곱 자리 수들을 나타내는 Set
			set = new HashSet<>();

			// 4X4 격자판
			map = new int[4][4];
			for (int i = 0; i < 4; i++) {
				for (int j = 0; j < 4; j++) {
					map[i][j] = sc.nextInt();
				}
			}

			// 일곱 자리 수 만들기
			for (int i = 0; i < 4; i++) {
				for (int j = 0; j < 4; j++) {
					String str = "" + map[i][j];
					dfs(i, j, 1, str);
				}
			}

			System.out.printf("#%d %d\n", t, set.size());
		}
	}

	// 일곱 자리 수 만들기
	static void dfs(int r, int c, int cnt, String str) {
		if (cnt == 7) {
			set.add(str);
			return;
		}

		// 북쪽으로 이동
		if (r - 1 >= 0) {
			dfs(r - 1, c, cnt + 1, str + map[r - 1][c]);
		}
		// 남쪽으로 이동
		if (r + 1 < 4) {
			dfs(r + 1, c, cnt + 1, str + map[r + 1][c]);
		}
		// 동쪽으로 이동
		if (c + 1 < 4) {
			dfs(r, c + 1, cnt + 1, str + map[r][c + 1]);
		}
		// 서쪽으로 이동
		if (c - 1 >= 0) {
			dfs(r, c - 1, cnt + 1, str + map[r][c - 1]);
		}
	}
}
