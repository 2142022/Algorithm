import java.util.Scanner;

public class 직사각형네개의합집합의면적구하기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 100 X 100 좌표
		int[][] map = new int[100][100];

		// 4개의 직사각형 입력받기
		for (int r = 0; r < 4; r++) {
			// 왼쪽 아래 꼭짓점의 좌표 (x1, y1)
			int x1 = sc.nextInt();
			int y1 = sc.nextInt();

			// 오른쪽 위 꼭짓점의 좌표 (x2, y2)
			int x2 = sc.nextInt();
			int y2 = sc.nextInt();

			// 직사각형이 있는 곳은 1, 아니면 0
			for (int i = x1; i < x2; i++) {
				for (int j = y1; j < y2; j++) {
					map[i][j] = 1;
				}
			}
		}

		// 직사각형의 면적의 합: map에서 1의 개수
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
}
