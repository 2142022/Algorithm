import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 미로1_BFS {

	// 미로
	static int[][] map;

	// 시작 지점
	static int[] start;

	// 도착 지점
	static int[] end;

	// 방문 체크
	static int[][] flag;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 10개의 테스트케이스
		for (int t = 1; t <= 10; t++) {
			// 테스트케이스 번호
			t = sc.nextInt();

			// 시작 지점과 도착 지점
			start = new int[2];
			end = new int[2];

			// 방문 체크
			flag = new int[16][16];

			// 16 X 16 미로
			map = new int[16][16];
			for (int i = 0; i < 16; i++) {
				// 문자열로 입력받은 후 char형 배열로 바꾸기
				char[] tmp = sc.next().toCharArray();

				for (int j = 0; j < 16; j++) {
					// char형을 int형으로 바꾸기
					map[i][j] = tmp[j] - '0';

					// 출발 지점과 도착 지점 찾기
					if (map[i][j] == 2) {
						start[0] = i;
						start[1] = j;
					} else if (map[i][j] == 3) {
						end[0] = i;
						end[1] = j;
					}
				}
			}

			if (bfs(start)) {
				System.out.printf("#%d %d\n", t, 1);
			} else {
				System.out.printf("#%d %d\n", t, 0);
			}
		}
	}

	private static boolean bfs(int[] start) {
		// 델타
		int[] dr = { -1, 1, 0, 0 };
		int[] dc = { 0, 0, -1, 1 };

		// 시작 지점을 큐에 넣고 방문 체크하기
		Queue<int[]> queue = new LinkedList<>();
		queue.offer(start);
		flag[start[0]][start[1]] = 1;

		// 큐에 원소가 없어질 때까지 반복
		while (!queue.isEmpty()) {
			// 첫 번째 원소 꺼내기 (현재 위치)
			int[] now = queue.poll();

			// 사방 탐색하기
			for (int i = 0; i < 4; i++) {
				int nr = now[0] + dr[i];
				int nc = now[1] + dc[i];

				// 도착하면 멈추기
				if (nr == end[0] && nc == end[1]) {
					return true;
				}

				// 통로라면
				if ((nr >= 0) && (nr < 16) && (nc >= 0) && (nc < 16) && (map[nr][nc] == 0)) {
					// 아직 방문하지 않았다면 큐에 넣고 방문 체크
					if (flag[nr][nc] == 0) {
						int[] tmp = { nr, nc };
						queue.offer(tmp);
						flag[nr][nc] = 1;
					}
				}
			}
		}

		return false;
	}
}
