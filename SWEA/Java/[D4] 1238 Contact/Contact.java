import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Contact {
	// 방문 체크
	static int[] visit;

	// 비상연락망 관계
	static int[][] relation;

	// 시작점부터의 거리
	static int[] dist;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 10개의 테스트케이스
		for (int t = 1; t <= 10; t++) {
			// 입력 받는 데이터의 길이
			int data = sc.nextInt();

			// 시작 번호
			int start = sc.nextInt();

			// 비상연락망 관계 (사람은 1부터 100까지 존재)
			// relation[i][j]: i번째 사람이 j번째 사람에게 연락을 할 수 있으면 1, 아니면 0
			relation = new int[101][101];
			for (int i = 0; i < data / 2; i++) {
				relation[sc.nextInt()][sc.nextInt()] = 1;
			}

			// 방문 체크
			visit = new int[101];

			// 시작점부터의 거리
			dist = new int[101];

			bfs(start);

			// 시작점으로부터의 거리가 가장 먼 사람 중 가장 큰 번호
			int max_dist = 0;
			int max_idx = 0;
			for (int i = 1; i < 101; i++) {
				if (dist[i] >= max_dist) {
					max_dist = dist[i];
					max_idx = i;
				}
			}

			System.out.printf("#%d %d\n", t, max_idx);
		}
	}

	private static void bfs(int start) {
		// 큐에 사람 번호와 시작점부터의 거리 넣기
		Queue<int[]> queue = new LinkedList<>();
		int[] tmp = { start, 0 };
		queue.offer(tmp);

		// 방문 체크
		visit[start] = 1;

		// 큐의 원소가 없어질 때까지 반복
		while (!queue.isEmpty()) {
			int[] now = queue.poll();

			// 현재 위치에서 연락할 수 있는 사람들의 번호 큐에 넣기
			for (int i = 1; i < 101; i++) {
				if ((visit[i] == 0) && (relation[now[0]][i] == 1)) {
					int[] next = { i, now[1] + 1 };
					queue.offer(next);
					dist[i] = now[1] + 1;
					visit[i] = 1;
				}
			}
		}
	}
}
