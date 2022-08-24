import java.util.Scanner;

public class 햄버거다이어트 {
	// 재료의 수
	static int N;

	// 제한 칼로리
	static int L;

	// 재료에 대한 점수와 칼로리
	static int[][] ingredient;

	// 점수가 높은 조합의 점수
	static int max;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 재료의 수
			N = sc.nextInt();

			// 제한 칼로리
			L = sc.nextInt();

			// 재료에 대한 점수와 칼로리
			ingredient = new int[N][2];
			for (int i = 0; i < N; i++) {
				ingredient[i][0] = sc.nextInt();
				ingredient[i][1] = sc.nextInt();
			}

			// 각 재료 조합마다의 점수 구하기
			max = 0;
			grade(0, 0, 0);

			// 출력
			System.out.printf("#%d %d\n", t, max);
		}
	}

	// 재료의 조합마다 점수 구하기
	private static void grade(int idx, int kcal, int result) {
		// kcal가 제한 칼로리 L보다 크다면 리턴
		if (kcal > L) {
			return;
		}

		// 아니면 max값과 비교
		else {
			max = Math.max(max, result);
		}

		// idx가 인덱스 범위를 넘어가면 리턴
		if (idx >= N) {
			return;
		}

		// 현재 재료를 사용할 때 재귀로 구하기
		grade(idx + 1, kcal + ingredient[idx][1], result + ingredient[idx][0]);

		// 현재 재료를 건너뛰고 재귀로 구하기
		grade(idx + 1, kcal, result);

	}
}
