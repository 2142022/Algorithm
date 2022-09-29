import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class 보급로 {
	// 출발 지점부터 (r, c)까지의 복구 작업 시간
	static class Road implements Comparable<Road> {
		int r, c, workTime;

		public Road(int r, int c, int workTime) {
			this.r = r;
			this.c = c;
			this.workTime = workTime;
		}

		@Override
		public int compareTo(Road o) {
			// 최소 힙
			return Integer.compare(this.workTime, o.workTime);
		}
	}

	// 지도의 크기
	static int N;

	// 지도
	static int[][] map;

	// 현재까지 작업한 최소 복구 시간
	static int[][] time;

	// 델타
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 지도의 크기
			N = sc.nextInt();

			// 지도
			map = new int[N][N];
			for (int i = 0; i < N; i++) {
				char[] tmp = sc.next().toCharArray();

				for (int j = 0; j < N; j++) {
					map[i][j] = tmp[j] - '0';
				}
			}

			// 현재까지 작업한 최소 복구 시간
			time = new int[N][N];
			for (int i = 0; i < N; i++) {
				Arrays.fill(time[i], Integer.MAX_VALUE);
			}

			// 다익스트라
			dijkstra();

			System.out.printf("#%d %d\n", t, time[N - 1][N - 1]);
		}
	}

	private static void dijkstra() {
		// 우선순위 큐 (최소 힙)
		PriorityQueue<Road> pq = new PriorityQueue<>();

		// 방문 체크
		int[][] visit = new int[N][N];

		// (0, 0)부터 시작
		pq.add(new Road(0, 0, 0));
		time[0][0] = 0;

		// 큐의 원소가 없어질 때까지 반복
		while (!pq.isEmpty()) {
			Road now = pq.poll();

			// 이미 방문했다면 넘어가기
			if (visit[now.r][now.c] == 1) {
				continue;
			}

			// 현재 위치 방문 체크
			visit[now.r][now.c] = 1;

			// 사방 탐색
			for (int i = 0; i < 4; i++) {
				int nr = now.r + dr[i];
				int nc = now.c + dc[i];

				// 범위를 초과하면 pass
				if ((nr < 0) || (nr >= N) || (nc < 0) || (nc >= N)) {
					continue;
				}

				// 방문하지 않았고 복구 시간을 더했을 때 기존에 저장해뒀던 값보다 작으면 바꾸기
				if ((visit[nr][nc] == 0) && (now.workTime + map[nr][nc] < time[nr][nc])) {
					time[nr][nc] = now.workTime + map[nr][nc];
					pq.add(new Road(nr, nc, time[nr][nc]));
				}
			}
		}
	}
}
