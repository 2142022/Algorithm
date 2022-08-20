import java.util.Scanner;

public class 가랏RC카 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 명령 수
			int N = sc.nextInt();

			// 속도
			int v = 0;
			// 이동 거리
			int s = 0;

			// N개의 명령
			for (int n = 0; n < N; n++) {
				// 명령
				int command = sc.nextInt();

				// 현재 속도 유지
				if (command == 0) {
					s += v;
				}

				// 가속
				else if (command == 1) {
					// 입력값만큼 속도 증가
					v += sc.nextInt();
					s += v;
				}

				// 감속
				else if (command == 2) {
					// 입력값만큼 속도 감소
					v -= sc.nextInt();

					// v가 음수라면 속도는 0이므로 더하지 않음
					if (v > 0) {
						s += v;
					} else {
						v = 0;
					}
				}
			}

			// 출력
			System.out.printf("#%d %d\n", t, s);
		}
	}
}
