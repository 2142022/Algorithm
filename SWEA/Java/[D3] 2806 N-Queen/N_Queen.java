import java.util.Scanner;

public class N_Queen {

	// 체스판 크기
	static int N;

	// 체스판
	static int[][] board;

	// 퀸을 놓는 방법의 수
	static int ans;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 체스판 크기
			N = sc.nextInt();

			// 체스판
			board = new int[N][N];

			// 퀸을 놓는 방법의 수
			ans = 0;

			// 퀸 놓기
			putQueen(0);

			System.out.printf("#%d %d\n", t, ans);
		}
	}

	private static void putQueen(int idx) {
		// N개의 퀸을 다 놓으면 끝내기
		if (idx == N) {
			ans++;
			return;
		}

		for (int i = 0; i < N; i++) {
			// (idx, i)에 퀸을 놓을 수 있는지 검사
			if (flag(idx, i)) {
				// 퀸을 놓으면 1로 만들기
				board[idx][i] = 1;
				putQueen(idx + 1);

				// 다음 경우를 위해 다시 0으로 초기화
				board[idx][i] = 0;
			}
		}
	}

	private static boolean flag(int r, int c) {
		int left = c;
		int right = c;

		// 상단의 3방향에 퀸이 있는지 확인
		for (int i = r - 1; i >= 0; i--) {
			left--;
			right++;

			// 상단에 퀸이 있는지 확인
			if (board[i][c] == 1) {
				return false;
			}

			// 왼쪽 상단에 퀸이 있는지 확인
			if ((left >= 0) && (board[i][left] == 1)) {
				return false;
			}

			// 오른쪽 상단에 퀸이 있는지 확인
			if ((right < N) && (board[i][right] == 1)) {
				return false;
			}
		}

		return true;
	}
}
