import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 입력받고 실행
		int T = sc.nextInt();
		for (int t = 1; t <= T; t++) {
			// 배열 크기, 단어 길이, 배열 입력받기
			int N = sc.nextInt();
			int K = sc.nextInt();
			int[][] map = new int[N][N];

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					map[i][j] = sc.nextInt();
				}
			}

			int cnt = 0;

			// 흰색부분(1)이 연속으로 K개 있으면 cnt++
			// 각 행 검색
			for (int i = 0; i < N; i++) {

				// 연속된 1의 개수
				int len = 0;

				for (int j = 0; j < N; j++) {
					if (map[i][j] == 1) {
						len++;
					} else {
						if (len == K) {
							cnt++;
						}
						len = 0;
					}
				}

				if (len == K)
					cnt++;
			}

			// 각 열 검색
			for (int j = 0; j < N; j++) {

				// 연속된 1의 개수
				int len = 0;

				for (int i = 0; i < N; i++) {
					if (map[i][j] == 1) {
						len++;
					} else {
						if (len == K) {
							cnt++;
						}
						len = 0;
					}
				}

				if (len == K)
					cnt++;
			}

			System.out.printf("#%d %d\n", t, cnt);
		}
	}
}
