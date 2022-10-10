import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 벽돌깨기 {
	// 구슬의 개수
	static int N;

	// map의 크기(H X W)
	static int H;
	static int W;

	// 남은 벽돌의 최소 개수
	static int min;

	// 델타
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 구슬의 개수
			N = sc.nextInt();

			// H X W 크기의 map
			W = sc.nextInt();
			H = sc.nextInt();
			int[][] map = new int[H][W];
			for (int i = 0; i < H; i++) {
				for (int j = 0; j < W; j++) {
					map[i][j] = sc.nextInt();
				}
			}

			// 남은 벽돌의 최소 개수
			min = Integer.MAX_VALUE;

			dfs(0, map);

			System.out.printf("#%d %d\n", t, min);
		}
	}

	// cnt: 구슬을 놓은 횟수
	private static void dfs(int cnt, int[][] map) {
		// 구슬을 다 쓰면 끝내기
		if (cnt == N) {
			min = Math.min(min, count(map));
			return;
		}

		// 구슬을 놓을 열 정하기
		for (int i = 0; i < W; i++) {
			// 현재 map과 동일한 정보 만들기
			int[][] tmp = new int[H][W];
			for (int r = 0; r < H; r++) {
				for (int c = 0; c < W; c++) {
					tmp[r][c] = map[r][c];
				}
			}

			// 처음 벽돌을 만나는 위치 찾기
			for (int j = 0; j < H; j++) {
				if (tmp[j][i] != 0) {
					// 벽돌 부수기
					bfs(j, i, tmp);
					break;
				}
			}

			// 공중에 떠 있는 벽돌 내리기
			down(tmp);

			dfs(cnt + 1, tmp);
		}
	}

	// 남은 벽돌의 개수 세기
	private static int count(int[][] map) {
		int result = 0;
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				if (map[i][j] != 0)
					result++;
			}
		}
		return result;
	}

	// 공중에 떠 있는 벽돌 내리기
	private static void down(int[][] map) {
		for (int j = 0; j < W; j++) {
			for (int i = H - 1; i >= 0; i--) {
				// 0이 있다면 다음 벽돌이 나타나는 곳 찾기
				if (map[i][j] == 0) {
					for (int k = i - 1; k >= 0; k--) {
						if (map[k][j] != 0) {
							map[i][j] = map[k][j];
							map[k][j] = 0;
							break;
						}
					}
				}
			}
		}
	}

	// (r, c)부터 벽돌 없애기
	private static void bfs(int r, int c, int[][] map) {
		// 시작위치
		int[] start = { r, c, map[r][c] };

		Queue<int[]> queue = new LinkedList<>();
		// 1이면 자기 자신만 부서지므로 사방 탐색이 필요없음
		if (map[r][c] > 1) {
			queue.offer(start);
		}
		map[r][c] = 0;

		// 큐의 원소가 없어질 때까지 반복
		while (!queue.isEmpty()) {
			// 현재 탐색 위치
			int[] now = queue.poll();

			// 사방 탐색
			for (int d = 1; d < now[2]; d++) {
				for (int i = 0; i < 4; i++) {
					int nr = now[0] + dr[i] * d;
					int nc = now[1] + dc[i] * d;

					// map 범위를 벗어나면 패스
					if (nr < 0 || nr >= H || nc < 0 || nc >= W) {
						continue;
					}

					// 깰 벽돌이 없으면 패스
					if (map[nr][nc] == 0) {
						continue;
					}

					// 벽돌 위치를 큐에 넣고 벽돌 부수기
					int[] next = { nr, nc, map[nr][nc] };

					// 1이면 자기 자신만 부서지므로 사방 탐색이 필요없음
					if (map[nr][nc] > 1) {
						queue.offer(next);
					}
					map[nr][nc] = 0;
				}
			}
		}
	}
}
