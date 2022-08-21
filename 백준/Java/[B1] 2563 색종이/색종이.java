import java.util.Scanner;

public class 색종이 {
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

		// 검은색 색종이가 놓은 영역의 넓이
		int area = 0;
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				if (map[i][j] == 1) {
					area++;
				}
			}
		}

		System.out.println(area);
	}

	static void check(int c, int r) {
		for (int i = c; i < c + 10; i++) {
			for (int j = r; j < r + 10; j++) {
				map[i][j] = 1;
			}
		}
	}
}
