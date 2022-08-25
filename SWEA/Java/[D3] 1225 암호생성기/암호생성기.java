import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 암호생성기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 10개의 테스트케이스
		for (int t = 1; t <= 10; t++) {
			StringBuilder sb = new StringBuilder();

			// 테스트케이스 번호 입력받기
			sc.nextInt();

			// 8개의 숫자 입력받기
			Queue<Integer> nums = new LinkedList<>();

			for (int i = 0; i < 8; i++) {
				nums.offer(sc.nextInt());
			}

			// 한 사이클 내에 poll 횟수
			int cnt = 0;

			// 0이 되면 break
			while (true) {
				cnt++;

				// 첫 원소 peek 후 감소
				int tmp = nums.poll() - cnt;
				if (tmp <= 0) {
					tmp = 0;
				}

				// 끝에 추가
				nums.offer(tmp);

				// tmp가 0이 되면 break
				if (tmp == 0) {
					break;
				}

				// 한 사이클이 지나면 cnt 초기화
				if (cnt == 5) {
					cnt = 0;
				}
			}

			sb.append("#" + t);
			while (!nums.isEmpty()) {
				sb.append(" " + nums.poll());
			}
			System.out.println(sb);
		}
	}
}