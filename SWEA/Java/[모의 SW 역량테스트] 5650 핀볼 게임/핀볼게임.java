import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class 핀볼게임 {
	// 핀볼 게임판의 크기
	static int N;

	// 핀볼 게임판 (테두리 설정하기 위해 +2)
	static int[][] map;

	// 웜홀 위치 및 번호
	static List<int[]> wormhole;

	// 블록들의 진행 방향 바꾸기
	// block[1][i] = j: i방향으로 블록1에 들어왔을 때 j방향으로 바꾸기
	// 0: 상, 1: 하, 2: 좌: 3: 우
	static int[][] block = { { 0, 0, 0, 0 }, { 1, 3, 0, 2 }, { 3, 0, 1, 2 }, { 2, 0, 3, 1 }, { 1, 2, 3, 0 },
			{ 1, 0, 3, 2 } };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 핀볼 게임판의 크기
			N = sc.nextInt();

			// 웜홀 위치 및 번호
			wormhole = new ArrayList<>();

			// 핀볼 게임판 (테두리 설정하기 위해 +2)
			map = new int[N + 2][N + 2];
			for (int i = 1; i < N + 1; i++) {
				for (int j = 1; j < N + 1; j++) {
					map[i][j] = sc.nextInt();

					// 웜홀
					if (map[i][j] >= 6) {
						int[] tmp = { i, j, map[i][j] };
						wormhole.add(tmp);
					}
				}
			}

			// 점수의 최대값
			int max = 0;

			// 출발 위치 및 진행 방향 설정
			for (int i = 1; i < N + 1; i++) {
				for (int j = 1; j < N + 1; j++) {
					// 블록, 블랙홀, 웜홀일 경우는 패스
					if (map[i][j] != 0) {
						continue;
					}

					// 진행 방향 (0: 상, 1: 하, 2: 좌, 3: 우)
					for (int d = 0; d < 4; d++) {
						max = Math.max(max, game(i, j, d));
					}
				}
			}

			System.out.printf("#%d %d\n", t, max);
		}
	}

	// (i, j)에서 d방향으로 게임을 시작했을 때의 점수
	private static int game(int startR, int startC, int d) {
		int score = 0;

		// 시작 위치 설정
		int r = startR;
		int c = startC;

		// 시작 위치로 돌아오면 끝내기 (무조건 한 번은 이동해야 하므로 do while문 사용)
		do {
			// 블랙홀에 도착하면 그만두기
			if (map[r][c] == -1) {
				break;
			}

			// 웜홀이라면 출구로 이동
			else if (map[r][c] >= 6) {
				// 웜홀 출구의 인덱스
				int idx = getWorm(r, c);
				r = wormhole.get(idx)[0];
				c = wormhole.get(idx)[1];
			}

			// 블록이라면 진행방향 바꾸기
			else if (map[r][c] >= 1 && map[r][c] <= 5) {
				score++;
				d = block[map[r][c]][d];
			}

			// 테두리라면 진행방향 바꾸기
			else if (r == 0) {
				score++;
				d = 1;
			} else if (r == N + 1) {
				score++;
				d = 0;
			} else if (c == 0) {
				score++;
				d = 3;
			} else if (c == N + 1) {
				score++;
				d = 2;
			}

			// 한 칸 이동
			if (d == 0) {
				r--;
			} else if (d == 1) {
				r++;
			} else if (d == 2) {
				c--;
			} else if (d == 3) {
				c++;
			}
		} while (r != startR || c != startC);

		return score;
	}

	// 웜홀 출구의 인덱스 찾기
	private static int getWorm(int r, int c) {
		int idx = -1;
		for (int i = 0; i < wormhole.size(); i++) {
			// 웜홀 값은 같으면서 위치는 다른 경우
			if ((wormhole.get(i)[2] == map[r][c]) && (wormhole.get(i)[0] != r || wormhole.get(i)[1] != c)) {
				idx = i;
				break;
			}
		}
		return idx;
	}
}
