import java.util.Scanner;

public class 직사각형 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 4개의 테스트케이스
		for (int t = 0; t < 4; t++) {
			// 첫 번째 사각형의 좌표 (x1, y1), (x2, y2)
			int x1 = sc.nextInt();
			int y1 = sc.nextInt();
			int x2 = sc.nextInt();
			int y2 = sc.nextInt();

			// 두 번째 사각형의 좌표 (x3, y3), (x4, y4)
			int x3 = sc.nextInt();
			int y3 = sc.nextInt();
			int x4 = sc.nextInt();
			int y4 = sc.nextInt();

			// 결과
			char result;

			// 겹치지 않는 경우
			if (x3 > x2 || x1 > x4 || y3 > y2 || y1 > y4) {
				result = 'd';
			}

			// 겹치는 부분이 점인 경우
			else if ((x1 == x4 && (y1 == y4 || y2 == y3)) || (x2 == x3 && (y1 == y4 || y2 == y3))) {
				result = 'c';
			}

			// 겹치는 부분이 선분인 경우
			else if (y1 == y4 || y2 == y3 || x1 == x4 || x2 == x3) {
				result = 'b';
			}

			// 겹치는 부분이 직사각형인 경우
			else {
				result = 'a';
			}

			System.out.println(result);
		}
	}
}
