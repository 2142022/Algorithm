import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 치즈도둑 {
	// 치즈 한 변의 길이
	static int N;

	// N X N 치즈
	static int[][] map;

	// 방문 체크
	static int[][] flag;

	// 델타
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 치즈 한 변의 길이
			N = sc.nextInt();

			// N X N 치즈
			map = new int[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					map[i][j] = sc.nextInt();
				}
			}

			// 치즈 덩어리가 가장 많을 때의 덩어리 개수
			// 처음에는 1개이므로 1로 초기화
			int max = 1;

			// x일이 지난 후 (100일이 지난 후에는 어차피 0이므로 제외)
			for (int x = 1; x < 100; x++) {
				// x일이 지난 후 치즈 상태
				for (int i = 0; i < N; i++) {
					for (int j = 0; j < N; j++) {
						// 맛있는 정도가 x인 칸을 0으로 만들기
						if (map[i][j] == x) {
							map[i][j] = 0;
						}
					}
				}

				// 덩어리의 개수
				int cheese = 0;

				// 방문 체크
				flag = new int[N][N];

				// 덩어리의 개수 구하기
				for (int i = 0; i < N; i++) {
					for (int j = 0; j < N; j++) {
						// 치즈가 남아있고, 아직 방문하지 않았을 때 덩어리의 시작
						if ((map[i][j] != 0) && (flag[i][j] == 0)) {
							cheese++;
							int[] start = { i, j };
							bfs(start);
						}
					}
				}

				// 현재 덩어리의 개수와 max 비교
				max = Math.max(max, cheese);
			}

			// 출력
			System.out.printf("#%d %d\n", t, max);
		}
	}

	// 현재 위치부터 연결된 덩어리 체크
	private static void bfs(int[] start) {
		// 큐에 현재 위치 추가하고 방문 체크
		Queue<int[]> queue = new LinkedList<>();
		queue.offer(start);
		flag[start[0]][start[1]] = 1;

		// 큐의 원소가 없어질 때까지 탐색
		while (!queue.isEmpty()) {
			// 큐의 원소 뽑기
			int[] now = queue.poll();

			// 사방 탐색하기
			for (int i = 0; i < 4; i++) {
				int nr = now[0] + dr[i];
				int nc = now[1] + dc[i];

				// 치즈가 있는 곳이고 방문하지 않았다면 큐에 추가하고 방문체크
				if ((nr >= 0) && (nr < N) && (nc >= 0) && (nc < N)) {
					if (map[nr][nc] != 0 && flag[nr][nc] == 0) {
						int[] tmp = { nr, nc };
						queue.offer(tmp);
						flag[nr][nc] = 1;
					}
				}
			}
		}
	}
}
