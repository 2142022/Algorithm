import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 퍼펙트셔플 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 카드 개수
			int N = sc.nextInt();

			// 카드 순서 입력받기
			Queue<String> queue1 = new LinkedList<>();
			Queue<String> queue2 = new LinkedList<>();
			for (int n = 0; n < N / 2; n++) {
				queue1.offer(sc.next());
			}

			// N이 홀수라면 queue1에 하나 더 집어넣기
			if (N % 2 == 1) {
				queue1.offer(sc.next());
			}
			
			for (int n = 0; n < N / 2; n++) {
				queue2.offer(sc.next());
			}

			// 출력
			System.out.print("#" + t);
			for (int i = 0; i < N / 2; i++) {
				System.out.print(" " + queue1.poll());
				System.out.print(" " + queue2.poll());
			}

			// queue1에 카드 하나가 더 있다면 출력
			if (!queue1.isEmpty()) {
				System.out.print(" " + queue1.poll());
			}

			System.out.println();
		}
	}
}