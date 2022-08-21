import java.util.Scanner;

public class 블랙잭 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 카드의 개수
		int N = sc.nextInt();

		// 딜러가 외치는 숫자
		int M = sc.nextInt();

		// N개의 카드
		int[] card = new int[N];
		for (int i = 0; i < N; i++) {
			card[i] = sc.nextInt();
		}

		// M에 최대한 가까운 카드
		int max = 0;

		// 3장의 카드 뽑기
		for (int i = 0; i < N - 2; i++) {
			for (int j = i + 1; j < N - 1; j++) {
				for (int k = j + 1; k < N; k++) {
					int tmp = card[i] + card[j] + card[k];

					if (tmp > M) {
						continue;
					} else {
						max = Math.max(max, tmp);
					}
				}
			}
		}

		System.out.println(max);
	}
}
