import java.util.Scanner;

public class 등산로조성 {

	// 지도 한 변의 길이
	static int N;

	// 최대 공사 가능 깊이
	static int K;

	// N X N 지도
	static int[][] map;

	// 방문 체크
	static int[][] visit;

	// 가장 긴 등산로의 길이
	static int max;

	// 델타
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 지도 한 변의 길이
			N = sc.nextInt();

			// 최대 공사 가능 깊이
			K = sc.nextInt();

			// 가장 높은 봉우리의 높이
			int maxH = 0;

			// N X N 지도
			map = new int[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					map[i][j] = sc.nextInt();
					maxH = Math.max(maxH, map[i][j]);
				}
			}

			// 가장 긴 등산로의 길이
			max = 1;

			// 가장 높은 봉우리부터 탐색
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (map[i][j] == maxH) {
						visit = new int[N][N];
						visit[i][j] = 1;
						dfs(i, j, 1, 0);
					}
				}
			}

			// 출력
			System.out.printf("#%d %d\n", t, max);
		}
	}

	// (r, c)에 연결된 등산로 구하기
	// length: 현재까지 연결된 등산로의 길이
	// flag: 공사를 했는지 체크 (했으면 1, 아니면 0)
	private static void dfs(int r, int c, int length, int flag) {
		// 사방이 현재 위치보다 봉우리의 높이가 크다면 끝내기
		if (check(r, c, flag)) {
			max = Math.max(max, length);
			return;
		}

		// 사방 탐색
		for (int i = 0; i < 4; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];

			if ((nr >= 0) && (nr < N) && (nc >= 0) && (nc < N)) {
				// 현 위치보다 크지만, 공사로 작아질 수 있는 경우
				if ((flag == 0) && (visit[nr][nc] == 0) && (map[nr][nc] >= map[r][c])
						&& (map[nr][nc] - K < map[r][c])) {
					// dfs 후에 공사 전 값으로 바꿔야 하므로 tmp로 저장
					int tmp = map[nr][nc];

					// (r, c)보다 하나만 작게 만들면 되므로 공사 K까지 할 필요 X
					map[nr][nc] = map[r][c] - 1;

					// 방문 체크
					visit[nr][nc] = 1;
					dfs(nr, nc, length + 1, 1);

					// 다시 공사 이전 값으로 바꾸기
					map[nr][nc] = tmp;

					// 방문 체크 해제
					visit[nr][nc] = 0;
				}

				// 현 위치보다 작다면 바로 탐색
				else if (map[nr][nc] < map[r][c]) {
					visit[nr][nc] = 1;
					dfs(nr, nc, length + 1, flag);
					visit[nr][nc] = 0;
				}
			}
		}
	}

	// (r, c)의 사방 봉우리가 더 큰지 확인
	private static boolean check(int r, int c, int flag) {
		for (int i = 0; i < 4; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];

			if ((nr >= 0) && (nr < N) && (nc >= 0) && (nc < N)) {
				// 현 위치보다 작은 경우
				if (map[nr][nc] < map[r][c]) {
					return false;
				}

				// 현 위치보다 크지만, 공사로 작아질 수 있는 경우
				else if ((flag == 0) && (visit[nr][nc] == 0) && (map[nr][nc] >= map[r][c])
						&& (map[nr][nc] - K < map[r][c])) {
					return false;
				}
			}
		}

		return true;
	}
}
