import java.util.PriorityQueue;
import java.util.Scanner;

public class 힙 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			StringBuilder sb = new StringBuilder();
			sb.append("#" + t + " ");

			// 우선순위 큐로 힙 생성
			PriorityQueue<Integer> heap = new PriorityQueue<>();

			// 수행할 연산의 수
			int N = sc.nextInt();

			// N개의 연산 수행
			for (int i = 0; i < N; i++) {
				// 연산 종류
				int op = sc.nextInt();

				// 연산1: 삽입
				if (op == 1) {
					//최소힙이 기본이기 때문에 최대힙이 되기 위해서 음수로 바꿔서 저장
					heap.add(-1 * sc.nextInt());
				}
				
				//연산2: 삭제
				else {
					//힙이 비어있다면 -1 리턴
					if (heap.isEmpty()) {
						sb.append(-1 + " ");
					} else {
						sb.append(-1 * heap.poll() + " ");
					}
				}
			}
			
			//출력
			System.out.println(sb);
		}
	}
}
