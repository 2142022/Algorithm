import java.util.Scanner;

public class 최빈수_구하기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수 입력받고 실행
		int T = sc.nextInt();

		for (int t = 0; t < T; t++) {
			// 테스트케이스 번호 입력받기
			int testcase = sc.nextInt();

			// 0~100까지의 점수를 나타내는 배열
			int[] scoreCnt = new int[101];

			// 학생 1000명의 점수를 입력받으면서 score_cnt 하나씩 추가하기
			for (int i = 0; i < 1000; i++) {
				scoreCnt[sc.nextInt()]++;
			}

			// cnt가 가장 많은 점수
			int maxScore = 0;

			// cnt 수가 많으면 maxScore로 바꾸기
			for (int i = 1; i < 101; i++) {

				// cnt 수가 같으면 최대값으로 저장해야 하므로 등호 넣기
				if (scoreCnt[i] >= scoreCnt[maxScore]) {
					maxScore = i;
				}
			}

			System.out.printf("#%d %d\n", testcase, maxScore);
		}
	}
}
