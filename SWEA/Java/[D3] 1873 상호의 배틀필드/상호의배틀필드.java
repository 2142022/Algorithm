import java.util.Scanner;

public class 상호의배틀필드 {
	// 맵의 높이 및 너비
	static int H;
	static int W;

	// 맵
	static char[][] map;

	// 현재 전차의 위치(행, 열) 및 방향 (상:1, 하:2, 좌:3, 우:4)
	static int R, C, D;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 맵의 높이 및 너비
			H = sc.nextInt();
			W = sc.nextInt();

			// 맵
			map = new char[H][W];
			for (int i = 0; i < H; i++) {
				map[i] = sc.next().toCharArray();
			}

			// 현재 전차의 위치(행, 열) 및 방향 (상:1, 하:2, 좌:3, 우:4)
			for (int i = 0; i < H; i++) {
				for (int j = 0; j < W; j++) {
					// 위를 바라보고 있을 때
					if (map[i][j] == '^') {
						R = i;
						C = j;
						D = 1;
					}

					// 아래를 바라보고 있을 때
					else if (map[i][j] == 'v') {
						R = i;
						C = j;
						D = 2;
					}

					// 왼쪽을 바라보고 있을 때
					else if (map[i][j] == '<') {
						R = i;
						C = j;
						D = 3;
					}

					// 오른쪽을 바라보고 있을 때
					else if (map[i][j] == '>') {
						R = i;
						C = j;
						D = 4;
					}
				}
			}

			// 사용자 입력 개수
			int N = sc.nextInt();

			// 사용자 입력
			char[] input = sc.next().toCharArray();

			// 사용자 입력 실행
			for (int i = 0; i < N; i++) {
				if (input[i] == 'S') {
					shoot();
				} else {
					go(input[i]);
				}
			}

			// 맵 출력
			System.out.printf("#" + t + " ");
			for (int i = 0; i < H; i++) {
				for (int j = 0; j < W; j++) {
					System.out.print(map[i][j]);
				}
				System.out.println();
			}
		}
	}

	// 포탄 발사
	static private void shoot() {
		// 상
		if (D == 1) {
			for (int i = R - 1; i >= 0; i--) {
				// 벽돌일 때는 평지로 바꾸기
				if (map[i][C] == '*') {
					map[i][C] = '.';
					break;
				}

				// 강철일 때는 소멸
				else if (map[i][C] == '#') {
					break;
				}
			}
		}

		// 하
		else if (D == 2) {
			for (int i = R + 1; i < H; i++) {
				// 벽돌일 때는 평지로 바꾸기
				if (map[i][C] == '*') {
					map[i][C] = '.';
					break;
				}

				// 강철일 때는 소멸
				else if (map[i][C] == '#') {
					break;
				}
			}
		}

		// 좌
		else if (D == 3) {
			for (int i = C - 1; i >= 0; i--) {
				// 벽돌일 때는 평지로 바꾸기
				if (map[R][i] == '*') {
					map[R][i] = '.';
					break;
				}

				// 강철일 때는 소멸
				else if (map[R][i] == '#') {
					break;
				}
			}
		}

		// 우
		else if (D == 4) {
			for (int i = C + 1; i < W; i++) {
				// 벽돌일 때는 평지로 바꾸기
				if (map[R][i] == '*') {
					map[R][i] = '.';
					break;
				}

				// 강철일 때는 소멸
				else if (map[R][i] == '#') {
					break;
				}
			}
		}
	}

	// 이동
	static private void go(char c) {
		// up
		if (c == 'U') {
			// 방향 바꾸기
			D = 1;
			map[R][C] = '^';

			// 인덱스가 범위안에 있고 평지면 이동
			if ((R >= 1) && (map[R - 1][C] == '.')) {

				// 전차가 있던 자리는 평지
				map[R][C] = '.';

				// 전차 이동
				map[R - 1][C] = '^';
				R--;
			}
		}

		// down
		else if (c == 'D') {
			// 방향 바꾸기
			D = 2;
			map[R][C] = 'v';

			// 인덱스가 범위안에 있고 평지면 이동
			if ((R < H - 1) && (map[R + 1][C] == '.')) {
				// 전차가 있던 자리는 평지
				map[R][C] = '.';

				// 전차 이동
				map[R + 1][C] = 'v';
				R++;
			}
		}

		// left
		else if (c == 'L') {
			// 방향 바꾸기
			D = 3;
			map[R][C] = '<';

			// 인덱스가 범위안에 있고 평지면 이동
			if ((C >= 1) && (map[R][C - 1] == '.')) {
				// 전차가 있던 자리는 평지
				map[R][C] = '.';

				// 전차 이동
				map[R][C - 1] = '<';
				C--;
			}
		}

		// right
		else if (c == 'R') {
			// 방향 바꾸기
			D = 4;
			map[R][C] = '>';

			// 인덱스가 범위안에 있고 평지면 이동
			if ((C < W - 1) && (map[R][C + 1] == '.')) {
				// 전차가 있던 자리는 평지
				map[R][C] = '.';

				// 전차 이동
				map[R][C + 1] = '>';
				C++;
			}
		}
	}
}