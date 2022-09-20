import java.util.Scanner;

public class 규영이와인영이의카드게임 {

	static int[] card1;
	static int[] card2;

	static int winCnt;
	static int loseCnt;

	static int[] result; // 인영이의 카드 경우의 수
	static int[] flag; // 인영이의 카드 중 사용했으면 1, 아니면 0

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 각 테스트케이스마다 초기화
			winCnt = loseCnt = 0;
			result = new int[9];
			flag = new int[9];

			// 총 카드
			int[] card = new int[19];
			// 규영이의 카드 입력받기
			for (int i = 0; i < 9; i++) {
				// 입력받은 카드는 1
				card[sc.nextInt()] = 1;
			}

			// 규영이의 카드
			card1 = new int[9];
			// 인영이의 카드
			card2 = new int[9];

			int m = 0;
			int n = 0;
			for (int i = 1; i < 19; i++) {
				// 1이면 규영이 카드, 0이면 인영이 카드
				if (card[i] == 1) {
					card1[m++] = i;
				} else {
					card2[n++] = i;
				}
			}

			// 순열로 인영이의 카드 순서 구하기
			permutation(0);

			System.out.printf("#%d %d %d\n", t, winCnt, loseCnt);
		}
	}

	static void permutation(int idx) {
		if (idx == 9) {
			// 규영이의 점수
			int score1 = 0;
			// 인영이의 점수
			int score2 = 0;

			for (int i = 0; i < 9; i++) {
				// 규영이의 카드가 더 크면 규영이 점수에 더하기
				if (card1[i] > result[i]) {
					score1 += card1[i] + result[i];
				} else {
					score2 += card1[i] + result[i];
				}
			}

			// 총 점수 비교하여 각각의 cnt 더하기 (무승부는 포함X)
			if (score1 > score2) {
				winCnt++;
			} else if (score1 < score2) {
				loseCnt++;
			}

			return;
		}

		// 9장의 카드 돌기
		for (int i = 0; i < 9; i++) {
			// 아직 사용하지 않았다면
			if (flag[i] == 0) {
				// 사용하기
				flag[i] = 1;
				result[idx] = card2[i];

				// 다음 카드 찾기
				permutation(idx + 1);

				// 사용한 후에는 다시 0 체크
				flag[i] = 0;
			}
		}
	}
}
