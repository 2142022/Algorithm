import java.util.Scanner;

public class 러시아국기같은깃발 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// N행 M열
			int N = sc.nextInt();
			int M = sc.nextInt();
			char[][] map = new char[N][M];
			for (int i = 0; i < N; i++) {
				char[] tmp = sc.next().toCharArray();
				for (int j = 0; j < M; j++) {
					map[i][j] = tmp[j];
				}
			}

			// cnt의 최소값
			int min = 2147483647;

			// W, B의 끝 행 번호: w, b
			for (int w = 0; w < N - 2; w++) {
				for (int b = w + 1; b < N - 1; b++) {
					min = Math.min(min, cnt(map, 0, w, 'W') + cnt(map, w + 1, b, 'B') + cnt(map, b + 1, N - 1, 'R'));
				}
			}

			// 출력
			System.out.printf("#%d %d\n", t, min);
		}
	}

	// 바꿔야 하는 칸 수 세기
	static int cnt(char[][] map, int r1, int r2, char c) {
		int result = 0;

		for (int i = r1; i <= r2; i++) {
			for (int j = 0; j < map[i].length; j++) {
				if (map[i][j] != c) {
					result++;
				}
			}
		}

		return result;
	}
}
