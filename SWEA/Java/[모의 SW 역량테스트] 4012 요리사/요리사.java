import java.util.Scanner;

public class 요리사 {

	// 식재료 수
	static int N;

	// 식재료들의 시너지
	static int[][] S;

	// 모든 식재료 (사용하면 1, 아니면 0)
	static int[] ingredient;

	// A음식의 식재료
	static int[] A;

	// B음식의 식재료
	static int[] B;

	// 최소의 음식 맛 차이
	static int min;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 식재료 수
			N = sc.nextInt();

			// 모든 식재료 (사용하면 1, 아니면 0)
			ingredient = new int[N];

			// A음식의 식재료
			A = new int[N / 2];

			// B음식의 식재료
			B = new int[N / 2];

			// 식재료들의 시너지
			S = new int[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					S[i][j] = sc.nextInt();
				}
			}

			// 최소의 음식 맛 차이
			min = 2147483647;

			// 식재료들의 조합 구하기
			combination(0, 0);

			System.out.printf("#%d %d\n", t, min);
		}
	}

	private static void combination(int idx, int cnt) {
		if (cnt == N / 2) {
			// A음식과 B음식의 식재료 구하기
			int m = 0;
			int n = 0;
			for (int i = 0; i < N; i++) {
				// 1이면 A음식, 0이면 B음식
				if (ingredient[i] == 1) {
					A[m++] = i;
				} else {
					B[n++] = i;
				}
			}
			// 현재 식재료들의 조합으로 음식 맛 차이 구하고 min과 비교
			min = Math.min(min, synergy());
			return;
		}

		for (int i = idx; i < N; i++) {
			// 사용한 재료 1로 체크
			ingredient[i] = 1;
			// 재귀로 다음 재료 구하기
			combination(i + 1, cnt + 1);
			// 다시 사용하지 않은 재료로 만들기
			ingredient[i] = 0;
		}
	}

	private static int synergy() {
		// A음식 식재료들의 시너지
		int synA = 0;
		for (int i : A) {
			for (int j : A) {
				synA += S[i][j];
			}
		}

		// B음식 식재료들의 시너지
		int synB = 0;
		for (int i : B) {
			for (int j : B) {
				synB += S[i][j];
			}
		}

		return Math.abs(synA - synB);
	}
}
