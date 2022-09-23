import java.util.Scanner;

public class 보호필름 {

	// 보호 필름의 두께
	static int D;

	// 보호 필름의 가로 길이
	static int W;

	// 합격 기준
	static int K;

	// 약품의 최소 투입 횟수
	static int min;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 보호 필름의 두께
			D = sc.nextInt();

			// 보호 필름의 가로 길이
			W = sc.nextInt();

			// 합격 기준
			K = sc.nextInt();

			// 셀들의 특성 (A: 0, B: 1)
			int[][] cell = new int[D][W];
			for (int i = 0; i < D; i++) {
				for (int j = 0; j < W; j++) {
					cell[i][j] = sc.nextInt();
				}
			}

			// 약품의 최소 투입 횟수
			min = D;

			input(cell, 0, 0);

			System.out.printf("#%d %d\n", t, min);
		}
	}

	// 인자: 현재 cell의 상태, 이번에 고칠 행의 인덱스, 현재까지의 약품 투입 횟수
	private static void input(int[][] status, int idx, int cnt) {
		// 합격 기준이 되면 현재까지의 투입 횟수와 min 비교
		if (pass(status)) {
			min = Math.min(min, cnt);
			return;
		}

		// 이미 cnt가 min보다 크다면 최소 투입 횟수 불가능하므로 리턴
		if (cnt >= min) {
			return;
		}

		// 모든 행을 변경했지만 불합격한 경우 리턴
		if ((idx == D) && (!pass(status))) {
			return;
		}

		// idx행 저장
		int[] tmp = new int[W];
		for (int i = 0; i < W; i++) {
			tmp[i] = status[idx][i];
		}

		// idx행 A로 변경
		for (int i = 0; i < W; i++) {
			status[idx][i] = 0;
		}
		input(status, idx + 1, cnt + 1);

		// idx행 B로 변경
		for (int i = 0; i < W; i++) {
			status[idx][i] = 1;
		}
		input(status, idx + 1, cnt + 1);

		// idx행 원래대로 변경
		for (int i = 0; i < W; i++) {
			status[idx][i] = tmp[i];
		}
		input(status, idx + 1, cnt);
	}

	// 입력받은 cell들의 상태가 합격인지 판단
	private static boolean pass(int[][] status) {
		for (int i = 0; i < W; i++) {
			// A나 B 중 연속하는 특성의 개수
			int cnt = 1;

			// 연속하는 특성의 최대 개수
			int max = 1;

			for (int j = 1; j < D; j++) {
				// 이전 cell과 특성이 같다면 cnt 증가
				if (status[j][i] == status[j - 1][i]) {
					cnt++;
				}

				// 다르다면 지금까지 연속한 특성의 개수와 max 비교하고 cnt는 1로 초기화
				else {
					max = Math.max(max, cnt);
					cnt = 1;
				}
			}

			// j = 6일때의 cnt와 비교
			max = Math.max(max, cnt);

			// max가 합격 기준 K에 미치지 못한다면 불합격
			if (max < K) {
				return false;
			}
		}

		return true;
	}
}
