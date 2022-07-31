import java.util.Scanner;

public class 회문1 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		// 10개의 테스트케이스
		for (int k = 0; k < 10; k++) {

			// 회문의 길이 입력받기
			int length = sc.nextInt();

			// 8X8 2차원 배열 입력받기
			char[][] map = new char[8][8];
			for (int i = 0; i < 8; i++) {
				String str = sc.next();

				for (int j = 0; j < 8; j++) {
					map[i][j] = str.charAt(j);
				}
			}

			// 회문의 개수
			int cnt = 0;

			// 회문의 개수 구하여 더하기
			for (int i = 0; i < 8; i++) {
				for (int j = 0; j < 9 - length; j++) {
					// 중간에 반복문을 빠져나왔는지 확인하기 위한 변수
					int flag = 1;

					// 행 기준
					for (int l = 0; l < length / 2; l++) {
						if (map[i][j + l] != map[i][j + length - l - 1]) {
							flag = 0;
							break;
						}
					}

					if (flag == 1) {
						cnt++;
					}

					flag = 1;

					// 열 기준
					for (int l = 0; l < length / 2; l++) {
						if (map[j + l][i] != map[j + length - l - 1][i]) {
							flag = 0;
							break;
						}
					}

					if (flag == 1) {
						cnt++;
					}

				}
			}

			System.out.printf("\n#%d %d", k + 1, cnt);
		}
	}
}