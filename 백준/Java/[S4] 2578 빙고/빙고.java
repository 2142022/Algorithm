import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 빙고 {
	// 빙고판 체크 (수가 불렸으면 1, 아니면 0)
	static int[][] flag = new int[5][5];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 빙고판 입력
		int[][] map = new int[5][5];
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				map[i][j] = sc.nextInt();
			}
		}

		// 사회자가 부르는 수
		Queue<Integer> nums = new LinkedList<>();
		for (int i = 0; i < 25; i++) {
			nums.offer(sc.nextInt());
		}

		// 사회자가 수를 부른 횟수
		int cnt = 0;

		// 빙고가 될 때까지 반복
		while (!bingo()) {
			cnt++;

			// 사회자가 부른 수
			int num = nums.poll();

			// 사회자가 부른 수가 있는 곳 체크
			for (int i = 0; i < 5; i++) {
				for (int j = 0; j < 5; j++) {
					if (map[i][j] == num) {
						flag[i][j] = 1;
					}
				}
			}
		}

		System.out.println(cnt);
	}

	// 빙고가 됐는지 확인
	static boolean bingo() {
		int result = 0;

		// 가로 확인
		for (int i = 0; i < 5; i++) {
			int cnt = 0;
			for (int j = 0; j < 5; j++) {
				if (flag[i][j] == 1) {
					cnt++;
				}
			}

			if (cnt == 5) {
				result++;
				if (result == 3) {
					return true;
				}
			}
		}

		// 세로 확인
		for (int i = 0; i < 5; i++) {
			int cnt = 0;
			for (int j = 0; j < 5; j++) {
				if (flag[j][i] == 1) {
					cnt++;
				}
			}

			if (cnt == 5) {
				result++;
				if (result == 3) {
					return true;
				}
			}
		}

		// 대각선 확인 (\ 방향)
		if (flag[0][0] == 1 && flag[1][1] == 1 && flag[2][2] == 1 && flag[3][3] == 1 && flag[4][4] == 1) {
			result++;
			if (result == 3) {
				return true;
			}
		}

		// 대각선 확인 (/ 방향)
		if (flag[0][4] == 1 && flag[1][3] == 1 && flag[2][2] == 1 && flag[3][1] == 1 && flag[4][0] == 1) {
			result++;
			if (result == 3) {
				return true;
			}
		}

		return false;
	}
}
