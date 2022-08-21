import java.util.Arrays;
import java.util.Scanner;

public class 진기의최고급붕어빵 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 손님 수
			int N = sc.nextInt();
			// M초 동안 K개의 붕어빵을 만듦
			int M = sc.nextInt();
			int K = sc.nextInt();

			// 손님 도착 시간 입력 받은 후 정렬
			int[] arrive = new int[N];
			for (int i = 0; i < N; i++) {
				arrive[i] = sc.nextInt();
			}
			Arrays.sort(arrive);

			// possibe = 1, impossible = 0
			int flag = 1;

			for (int i = 0; i < N; i++) {
				// 손님이 온 시간에 남아있는 붕어빵의 개수
				int cnt = K * (arrive[i] / M) - (i + 1);

				// cnt가 음수라면 불가능
				if (cnt < 0) {
					flag = 0;
					break;
				}
			}

			// 출력
			if (flag == 1) {
				System.out.printf("#%d Possible\n", t);
			} else {
				System.out.printf("#%d Impossible\n", t);
			}
		}
	}
}
