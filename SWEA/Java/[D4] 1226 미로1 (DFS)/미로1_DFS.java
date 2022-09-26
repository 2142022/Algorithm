import java.util.Scanner;

public class 미로1_DFS {

	// 미로
	static int[][] map;

	// 도착 지점
	static int[] end;

	// 방문 체크
	static int[][] flag;

	// 델타
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	// 결과 (도착 지점에 갈 수 있으면 1, 아니면 0)
	static int result;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 10개의 테스트케이스
		for (int t = 1; t <= 10; t++) {
			// 테스트케이스 번호
			t = sc.nextInt();

			// 시작 지점과 도착 지점
			int[] start = new int[2];
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

			// 결과 초기화
			result = 0;

			dfs(start);
			System.out.printf("#%d %d\n", t, result);
		}
	}

	private static void dfs(int[] now) {
		// 도착했다면 결과 1로 만들고 리턴
		if ((now[0] == end[0]) && (now[1] == end[1])) {
			result = 1;
			return;
		}

		// 현재 위치 방문 체크
		flag[now[0]][now[1]] = 1;

		// 사방 탐색
		for (int i = 0; i < 4; i++) {
			int nr = now[0] + dr[i];
			int nc = now[1] + dc[i];

			// 통로라면
			if ((nr >= 0) && (nr < 16) && (nc >= 0) && (nc < 16) && (map[nr][nc] != 1)) {
				// 아직 방문하지 않았다면 재귀로 탐색
				if (flag[nr][nc] == 0) {
					int[] tmp = { nr, nc };
					dfs(tmp);

					if (result == 1) {
						return;
					}
				}
			}
		}
	}
}
