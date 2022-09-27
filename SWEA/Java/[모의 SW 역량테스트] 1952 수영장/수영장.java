import java.util.Scanner;

public class 수영장 {

	// 이용권 요금 (0: 1일 이용권, 1: 1달 이용권, 2: 3달 이용권, 3: 1년 이용권)
	static int[] ticket;

	// 12개월 이용 계획
	static int[] plan;

	// 마지막으로 이용하는 달 + 1
	static int last;

	// 가장 적게 지출하는 비용
	static int min;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 이용권 요금 (0: 1일 이용권, 1: 1달 이용권, 2: 3달 이용권, 3: 1년 이용권)
			ticket = new int[4];
			for (int i = 0; i < 4; i++) {
				ticket[i] = sc.nextInt();
			}

			// 마지막으로 이용하는 달
			last = 0;

			// 12개월 이용 계획
			plan = new int[13];
			for (int i = 1; i < 13; i++) {
				plan[i] = sc.nextInt();

				// 이용하는 날 수가 0이 아니라면 last 바꾸기
				last = plan[i] != 0 ? i : last;
			}

			// 하루도 이용하지 않는다면 0 출력 후 끝내기
			if (last == 0) {
				System.out.printf("#%d %d\n", t, 0);
				continue;
			}

			// 가장 적게 지출하는 비용
			// 처음에는 1년 이용 계획으로 초기화
			min = ticket[3];

			// 가격 구하기
			getPrice(1, 0);

			// 출력
			System.out.printf("#%d %d\n", t, min);
		}
	}

	// r번째 달의 가격 구하기
	// price: 현재까지의 가격
	private static void getPrice(int r, int price) {
		// 마지막으로 이용하는 달보다 크게 된다면 끝내기
		if (r > last) {
			min = Math.min(min, price);
			return;
		}

		// 3달 이용권 사용하는 경우
		getPrice(r + 3, price + ticket[2]);

		// 1달 이용권 사용하는 경우
		getPrice(r + 1, price + ticket[1]);

		// 1일 이용권 사용하는 경우
		getPrice(r + 1, price + plan[r] * ticket[0]);
	}
}
