import java.util.Scanner;

public class 파동파동 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			StringBuilder sb = new StringBuilder();

			// 배열의 크기
			int N = sc.nextInt();

			// 파동 시작값
			int M = sc.nextInt();

			// 파동 시작 행과열
			int R = sc.nextInt();
			int C = sc.nextInt();

			// 증감값
			int D = sc.nextInt();

			// 배열
			int[][] map = new int[N][N];

			// 첫 행부터 파원이 있는 행까지
			for (int i = 0; i < R; i++) {
				for (int j = Math.max(0, C - R + i); j <= Math.min(N - 1, R + C - i - 2); j++) {
					int num = M + D * (R - 1 - i);
					if (num < 0) {
						num = 0;
					} else if (num > 255) {
						num = 255;
					}
					map[i][j] = num;
				}

				int j = C - R + i - 1;
				while (j >= 0) {
					int num = map[i][j + 1] + D;
					if (num < 0) {
						num = 0;
					} else if (num > 255) {
						num = 255;
					}
					map[i][j] = num;
					j--;
				}

				j = R + C - i - 1;
				while (j < N) {
					int num = map[i][j - 1] + D;
					if (num < 0) {
						num = 0;
					} else if (num > 255) {
						num = 255;
					}
					map[i][j] = num;
					j++;
				}
			}

			// 파원 다음 행부터 끝 행까지
			for (int i = R; i < N; i++) {
				for (int j = Math.max(0, R + C - i - 2); j <= Math.min(N - 1, C - R + i); j++) {
					int num = M + D * (i - R + 1);
					if (num < 0) {
						num = 0;
					} else if (num > 255) {
						num = 255;
					}
					map[i][j] = num;
				}

				int j = R + C - i - 3;
				while (j >= 0) {
					int num = map[i][j + 1] + D;
					if (num < 0) {
						num = 0;
					} else if (num > 255) {
						num = 255;
					}
					map[i][j] = num;
					j--;
				}

				j = C - R + i + 1;
				while (j < N) {
					int num = map[i][j - 1] + D;
					if (num < 0) {
						num = 0;
					} else if (num > 255) {
						num = 255;
					}
					map[i][j] = num;
					j++;
				}
			}

			sb.append("#" + t);

			// 각 행의 합 구하기
			for (int i = 0; i < N; i++) {
				int sum = 0;
				for (int j = 0; j < N; j++) {
					sum += map[i][j];
				}

				sb.append(" " + sum);
			}

			System.out.println(sb);
		}
	}
}