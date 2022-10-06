import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 탈주범검거 {
	// 지도
	static int[][] map;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 지도의 크기: N X M
			int N = sc.nextInt();
			int M = sc.nextInt();

			// 맨홀 뚜껑의 위치와 그때 위치한 시간(1)
			int[] start = new int[3];
			start[0] = sc.nextInt();
			start[1] = sc.nextInt();
			start[2] = 1;

			// 탈출 후 소요된 시간
			int L = sc.nextInt();

			// 지도
			map = new int[N][M];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					map[i][j] = sc.nextInt();
				}
			}

			// 탈주범이 위치할 수 있는 장소의 개수
			int cnt = 0;

			// 방문 체크
			int[][] visit = new int[N][M];

			// 델타
			int[] dr = { -1, 1, 0, 0 };
			int[] dc = { 0, 0, -1, 1 };

			// 큐에 시작 지점 넣기
			Queue<int[]> queue = new LinkedList<>();
			queue.offer(start);
			visit[start[0]][start[1]] = 1;

			// 큐의 원소가 빌 때까지 반복
			while (!queue.isEmpty()) {
				// 현재 위치
				int[] now = queue.poll();

				// 시간이 넘어가면 끝내기
				if (now[2] > L) {
					break;
				}

				cnt++;

				// 사방 탐색
				for (int i = 0; i < 4; i++) {
					int nr = now[0] + dr[i];
					int nc = now[1] + dc[i];

					// 범위를 벗어나면 패스
					if ((nr < 0) || (nr >= N) || (nc < 0) || (nc >= M)) {
						continue;
					}

					// 방문을 했거나 터널이 연결되어 있지 않으면 패스
					if (visit[nr][nc] == 1 || !check(i, now[0], now[1], nr, nc)) {
						continue;
					}

					// queue에 다음 위치 넣기
					int[] tmp = { nr, nc, now[2] + 1 };
					queue.offer(tmp);
					visit[nr][nc] = 1;
				}
			}

			System.out.printf("#%d %d\n", t, cnt);
		}
	}

	// 현재 위치(r, c)에서 (nr, nc)로 갈 수 있는지 체크
	private static boolean check(int idx, int r, int c, int nr, int nc) {
		// 상으로 가려고 하는 경우
		if (idx == 0) {
			if (map[r][c] == 1 || map[r][c] == 2 || map[r][c] == 4 || map[r][c] == 7) {
				if (map[nr][nc] == 1 || map[nr][nc] == 2 || map[nr][nc] == 5 || map[nr][nc] == 6) {
					return true;
				}
			}
		}

		// 하로 가려고 하는 경우
		else if (idx == 1) {
			if (map[r][c] == 1 || map[r][c] == 2 || map[r][c] == 5 || map[r][c] == 6) {
				if (map[nr][nc] == 1 || map[nr][nc] == 2 || map[nr][nc] == 4 || map[nr][nc] == 7) {
					return true;
				}
			}
		}

		// 좌로 가려고 하는 경우
		else if (idx == 2) {
			if (map[r][c] == 1 || map[r][c] == 3 || map[r][c] == 6 || map[r][c] == 7) {
				if (map[nr][nc] == 1 || map[nr][nc] == 3 || map[nr][nc] == 4 || map[nr][nc] == 5) {
					return true;
				}
			}
		}

		// 우로 가려고 하는 경우
		else if (idx == 3) {
			if (map[r][c] == 1 || map[r][c] == 3 || map[r][c] == 4 || map[r][c] == 5) {
				if (map[nr][nc] == 1 || map[nr][nc] == 3 || map[nr][nc] == 6 || map[nr][nc] == 7) {
					return true;
				}
			}
		}

		return false;
	}
}
