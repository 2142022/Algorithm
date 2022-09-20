import java.util.Scanner;

public class 부분수열의합 {
	// 자연수 개수
	static int N;

	// 부분 수열의 합
	static int K;

	// N개의 자연수
	static int[] nums;

	// 결과: 부분 수열의 합이 K가 되는 경우의 수
	static int cnt;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 자연수 개수
			N = sc.nextInt();

			// 부분 수열의 합
			K = sc.nextInt();

			// N개의 자연수
			nums = new int[N];
			for (int i = 0; i < N; i++) {
				nums[i] = sc.nextInt();
			}

			// 결과: 부분 수열의 합이 K가 되는 경우의 수
			cnt = 0;
			powerSet(0, 0);

			System.out.printf("#%d %d\n", t, cnt);
		}
	}

	// 부분 수열의 합이 K가 되는 경우의 수
	static void powerSet(int idx, int sum) {
		// sum이 K가 되면 cnt 증가
		if (sum == K) {
			cnt++;
			return;
		}

		// sum이 K보다 크면 그만두기
		else if (sum > K) {
			return;
		}

		// idx가 인데스 범위를 넘어가면 그만두기
		if (idx >= N) {
			return;
		}

		// 현재 수 더하고 다음 인덱스로 넘어가기
		powerSet(idx + 1, sum + nums[idx]);

		// 현재 수 건너뛰기
		powerSet(idx + 1, sum);
	}
}
