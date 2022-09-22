import java.util.Scanner;

public class 최적경로 {
	// 고객의 수
	static int N;

	// 회사의 위치
	static int workX;
	static int workY;

	// 집의 위치
	static int homeX;
	static int homeY;

	// 고객의 위치
	static int[][] customer;

	// 고객 순서 (모든 경우)
	static int[][] result;

	// 고객 방문 체크
	static int[] flag;

	// 최단 이동거리
	static int min;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 고객의 수
			N = sc.nextInt();

			// 회사의 위치
			workX = sc.nextInt();
			workY = sc.nextInt();

			// 집의 위치
			homeX = sc.nextInt();
			homeY = sc.nextInt();

			// N명의 고객의 위치
			customer = new int[N][2];
			for (int i = 0; i < N; i++) {
				customer[i][0] = sc.nextInt();
				customer[i][1] = sc.nextInt();
			}

			// 고객 순서 (모든 경우)
			result = new int[N][2];

			// 고객 방문 체크
			flag = new int[N];

			// 최단 이동거리
			min = 2147483647;

			// 인자: 몇 번째 고객인지, 현재까지의 이동거리
			distance(0, 0);

			System.out.printf("#%d %d\n", t, min);
		}
	}

	private static void distance(int idx, int d) {
		// 고객의 순서를 모두 확정했을 때 마지막 고객과 집까지의 이동거리를 추가하여 min과 비교
		if (idx == N) {
			d += Math.abs(homeX - result[idx - 1][0]) + Math.abs(homeY - result[idx - 1][1]);
			min = Math.min(d, min);
			return;
		}

		for (int i = 0; i < N; i++) {
			// 방문한 고객은 pass
			if (flag[i] == 1) {
				continue;
			}

			// 방문 체크
			flag[i] = 1;
			result[idx] = customer[i];

			// 이전 고객 또는 회사에서부터의 거리
			int tmp;
			if (idx == 0) {
				tmp = Math.abs(result[idx][0] - workX) + Math.abs(result[idx][1] - workY);
			} else {
				tmp = Math.abs(result[idx][0] - result[idx - 1][0]) + Math.abs(result[idx][1] - result[idx - 1][1]);
			}

			// 현재까지의 이동거리가 min보다 작을 때만 실행
			// 크면 어차피 min 불가
			if (d + tmp < min) {
				distance(idx + 1, d + tmp);
			}
			flag[i] = 0;
		}
	}
}
