import java.util.Scanner;

public class 달팽이_숫자 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수 입력받고 실행
		int T = sc.nextInt();
		for (int t = 1; t <= T; t++) {

			// 달팽이 크기
			int N = sc.nextInt();

			int tmp = N;

			int[][] arr = new int[N][N];
			int num = 1;

			int i = 0;
			int j = -1;

			while (num <= N * N) {
				for (int n = 0; n < tmp; n++) {
					arr[i][++j] = num++;
				}

				if (--tmp == 0) {
					break;
				}

				for (int n = 0; n < tmp; n++) {
					arr[++i][j] = num++;
				}

				for (int n = 0; n < tmp; n++) {
					arr[i][--j] = num++;
				}

				if (--tmp == 0) {
					break;
				}

				for (int n = 0; n < tmp; n++) {
					arr[--i][j] = num++;
				}
			}

			System.out.printf("#%d\n", t);
			for (int r = 0; r < N; r++) {
				for (int c = 0; c < N; c++) {
					System.out.printf("%d ", arr[r][c]);
				}
				System.out.println();
			}
		}
	}
}
