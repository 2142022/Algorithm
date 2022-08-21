import java.util.Scanner;

public class 색종이2 {
	// 도화지 상태 (검은색 색종이가 놓이면 1, 없으면 0)
	static int[][] map = new int[100][100];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 색종이 수
		int N = sc.nextInt();

		// 검은색 색종이 위치 입력받기
		int[][] black = new int[N][2];
		for (int i = 0; i < N; i++) {
			black[i][0] = sc.nextInt();
			black[i][1] = sc.nextInt();
		}

		// 도화지 상태 체크하기
		for (int i = 0; i < N; i++) {
			check(black[i][0], black[i][1]);
		}

		// 검은색 색종이가 놓은 영역의 둘레의 길이: 색종이가 놓여있고 사방에 색종이가 없는 경우 +1
		int len = 0;
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				if (map[i][j] == 1) {
					// 상
					if ((i + 1 < 100) && (map[i + 1][j] == 0)) {
						len++;
					}

					// 하
					if ((i - 1 >= 0) && (map[i - 1][j] == 0)) {
						len++;
					}

					// 좌
					if ((j - 1 >= 0) && (map[i][j - 1] == 0)) {
						len++;
					}

					// 우
					if ((j + 1 < 100) && (map[i][j + 1] == 0)) {
						len++;
					}
				}
			}
		}

		// 색종이가 도화지의 끝에 놓여 있는 경우
		for (int i = 0; i < 100; i++) {
			if (map[i][0] == 1 || map[i][99] == 1) {
				len++;
			}
			if (map[0][i] == 1 || map[99][i] == 1) {
				len++;
			}
		}

		System.out.println(len);
	}

	static void check(int c, int r) {
		for (int i = c; i < c + 10; i++) {
			for (int j = r; j < r + 10; j++) {
				map[i][j] = 1;
			}
		}
	}
}
