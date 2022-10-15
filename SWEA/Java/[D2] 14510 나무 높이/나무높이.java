import java.util.Scanner;

public class 나무높이 {
	// 0: 짝수날 물을 주는 횟수, 1: 홀수날 물을 주는 횟수
	static int[] cnt;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 나무의 개수
			int N = sc.nextInt();

			// 가장 높은 나무의 높이
			int maxH = 0;

			// 나무들의 높이
			int[] tree = new int[N];
			for (int i = 0; i < N; i++) {
				tree[i] = sc.nextInt();
				maxH = Math.max(maxH, tree[i]);
			}

			// 0: 짝수날 물을 주는 횟수, 1: 홀수날 물을 주는 횟수
			cnt = new int[2];

			// 가장 높은 나무와의 높이 차가 홀수인 경우 홀수날에 +1
			// 어차피 다른 나무와 같은 날에 물을 줄 수 없기 때문
			for (int i = 0; i < N; i++) {
				if (tree[i] != maxH) {
					// 나무 높이의 차
					int diff = maxH - tree[i];

					if (diff % 2 == 1) {
						cnt[1]++;
						tree[i]++;
					}
				}
			}

			// 각 나무마다 물을 줘야 하는 횟수 구하기
			for (int i = 0; i < N; i++) {
				if (tree[i] != maxH) {
					getCnt(maxH - tree[i]);
				}
			}

			int result = 0;

			// 짝수날이 홀수날보다 크거나 같은 경우
			if (cnt[0] >= cnt[1]) {
				result = 2 * cnt[0];
			}

			// 홀수날이 짝수날보다 큰 경우
			else {
				result = 2 * cnt[1] - 1;
			}

			System.out.printf("#%d %d\n", t, result);
		}
	}

	// 나무 높이 차가 i일 때 물을 줘야 하는 날 수 구하기
	private static void getCnt(int diff) {
		// 높이 차가 0이 될 때까지 반복
		while (diff != 0) {
			// 짝수날이 홀수날보다 크다면 홀수날 +2
			if (cnt[0] > cnt[1]) {
				cnt[1] += 2;
			}

			// 홀수날이 짝수날보다 크거나 같다면 짝수날 +1
			else {
				cnt[0]++;
			}

			// 높이 차를 2씩 감소시키기
			diff -= 2;
		}
	}
}
