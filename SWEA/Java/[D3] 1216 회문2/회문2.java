import java.util.Scanner;

public class 회문2 {

	// 100X100 글자판
	static char[][] map = new char[100][100];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 10개의 테스트케이스
		for (int t = 0; t < 10; t++) {
			// 테스트케이스 번호 입력받기
			int testcase = sc.nextInt();

			// 100X100 글자판 입력받기
			for (int i = 0; i < 100; i++) {
				String str = sc.next();
				map[i] = str.toCharArray();
			}

			// 회문 길이 최대값 (기본으로 1 설정)
			int max = 1;

			// 자리를 돌면서 좌우 비교
			for (int i = 0; i < 100; i++) {
				for (int j = 1; j < 99; j++) {
					max = Math.max(max, row_palindrome(i, j));
				}
			}

			// 자리를 돌면서 위아래 비교
			for (int j = 0; j < 100; j++) {
				for (int i = 1; i < 99; i++) {
					max = Math.max(max, col_palindrome(i, j));
				}
			}

			System.out.printf("#%d %d\n", testcase, max);
		}
	}

	static int row_palindrome(int row, int col) {
		// 회문 길이
		int result1 = 1;

		// 이동 거리
		int i = 1;

		// 회문의 길이가 홀수일 때
		while ((col - i >= 0) && (col + i < 100)) {
			// 좌우가 같으면 회문길이 +2
			if (map[row][col - i] == map[row][col + i]) {
				result1 += 2;
			} else {
				break;
			}
			i++;
		}

		i = 1;
		int result2 = 2;

		// 회문의 길이가 짝수일 때
		if (map[row][col] == map[row][col + 1]) {
			while ((col - i >= 0) && (col + 1 + i < 100)) {
				// 좌우가 같으면 회문길이 +2
				if (map[row][col - i] == map[row][col + 1 + i]) {
					result2 += 2;
				} else {
					break;
				}
				i++;
			}
		}

		return Math.max(result1, result2);
	}

	static int col_palindrome(int row, int col) {
		// 회문 길이
		int result1 = 1;

		// 이동 거리
		int i = 1;

		// 회문의 길이가 홀수일 때
		while ((row - i >= 0) && (row + i < 100)) {
			// 위아래가 같으면 회문길이 +2
			if (map[row - i][col] == map[row + i][col]) {
				result1 += 2;
			} else {
				break;
			}
			i++;
		}

		i = 1;
		int result2 = 2;

		// 회문의 길이가 짝수일 때
		if (map[row][col] == map[row + 1][col]) {
			while ((row - i >= 0) && (row + 1 + i < 100)) {
				// 위아래가 같으면 회문길이 +2
				if ((map[row - i][col]) == map[row + 1 + i][col]) {
					result2 += 2;
				} else {
					break;
				}
				i++;
			}
		}

		return Math.max(result1, result2);
	}
}