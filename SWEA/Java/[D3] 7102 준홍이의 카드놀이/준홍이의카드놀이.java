import java.util.Scanner;

public class 준홍이의카드놀이 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			StringBuilder sb = new StringBuilder();

			// 두 개의 정수 N, M
			int N = sc.nextInt();
			int M = sc.nextInt();

			// N, M 크기의 배열
			int[] num1 = new int[N];
			int[] num2 = new int[M];

			for (int i = 0; i < N; i++) {
				num1[i] = i + 1;
			}

			for (int i = 0; i < M; i++) {
				num2[i] = i + 1;
			}

			// N + M + 1 크기의 배열
			int[] cnt = new int[N + M + 1];

			// 카드를 더한 값 체크
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					cnt[num1[i] + num2[j]]++;
				}
			}

			// 가장 높은 확률
			int max = 0;
			for (int i = 0; i < N + M + 1; i++) {
				if (cnt[i] > max) {
					max = cnt[i];
				}
			}

			sb.append("#" + t);

			// cnt는 이미 오름차순이므로 확률이 높은 값 순서대로 append
			for (int i = 0; i < N + M + 1; i++) {
				if (cnt[i] == max) {
					sb.append(" " + i);
				}
			}

			System.out.println(sb);
		}
	}
}