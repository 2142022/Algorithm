import java.util.Scanner;

public class 농작물수확하기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스
		int T = sc.nextInt();

		// T개의 테스트 케이스
		for (int t = 1; t <= T; t++) {
			// 농장의 크기
			int N = sc.nextInt();

			// 농작물의 가치 입력받기
			int[][] value = new int[N][N];
			for (int i = 0; i < N; i++) {
				// char로 입력받은 후 int로 바꾸기
				char[] tmp = sc.next().toCharArray();

				for (int j = 0; j < N; j++) {
					value[i][j] = tmp[j] - '0';
				}
			}

			// 수익 계산하기
			// N / 2번째 행까지는 +2칸씩 늘어남
			int cnt = 1;
			int revenue = 0;
			for (int i = 0; i <= N / 2; i++) {
				for (int j = 0; j < N; j++) {
					// 행과 열 인덱스의 합이 N/2인 곳부터 cnt개 더하기
					if (i + j == N / 2) {
						for (int c = 0; c < cnt; c++) {
							revenue += value[i][j + c];
						}
						break;
					}
				}
				cnt += 2;
			}

			// 그 뒤로는 -2칸씩 줄어듦
			cnt -= 4;
			for (int i = N / 2 + 1; i < N; i++) {
				for (int j = 0; j < N; j++) {
					// 행과 열 인덱스의 차가 N/2인 곳부터 cnt개 더하기
					if (i - j == N / 2) {
						for (int c = 0; c < cnt; c++) {
							revenue += value[i][j + c];
						}
						break;
					}
				}
				cnt -= 2;
			}

			// 출력
			System.out.printf("#%d %d\n", t, revenue);
		}
	}
}
