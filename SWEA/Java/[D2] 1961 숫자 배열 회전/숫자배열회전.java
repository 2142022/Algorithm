import java.util.Scanner;

public class 숫자배열회전 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 배열 크기
			int N = sc.nextInt();

			// 배열
			int[][] map = new int[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					map[i][j] = sc.nextInt();
				}
			}

			// 90도 회전
			int[][] result1 = new int[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					result1[i][j] = map[N - j - 1][i];
				}
			}

			// 180도 회전
			int[][] result2 = new int[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					result2[i][j] = map[N - i - 1][N - j - 1];
				}
			}

			// 270도 회전
			int[][] result3 = new int[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					result3[i][j] = map[j][N - i - 1];
				}
			}

			// 출력
			System.out.println("#" + t + " ");
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					System.out.print(result1[i][j]);
				}
				System.out.print(" ");
				for (int j = 0; j < N; j++) {
					System.out.print(result2[i][j]);
				}
				System.out.print(" ");
				for (int j = 0; j < N; j++) {
					System.out.print(result3[i][j]);
				}
				System.out.println();
			}
		}
	}
}
