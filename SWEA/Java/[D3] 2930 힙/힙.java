import java.util.Scanner;

public class 힙 {
	static Scanner sc = new Scanner(System.in);

	// 최대 힙을 나타내는 배열
	static int[] heap;

	// 현재 원소의 개수
	static int size;

	public static void main(String[] args) {
		// 출력할 결과
		StringBuilder sb;

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 출력할 결과
			sb = new StringBuilder();

			size = 0;

			// 수행해야 하는 연산의 수
			int N = sc.nextInt();

			// 최대 힙을 나타내는 배열
			heap = new int[N + 1];

			sb.append("#" + t + " ");

			// N번의 연산
			for (int n = 0; n < N; n++) {
				// 연산 종류 입력받기
				int op = sc.nextInt();

				// 연산 1: 삽입
				if (op == 1) {
					size++;
					add();
				}

				// 연산2: 삭제
				else {
					sb.append(del() + " ");
				}
			}

			// 출력
			System.out.println(sb);
		}
	}

	static void add() {
		// 숫자 삽입
		int num = sc.nextInt();
		heap[size] = num;

		// 최대 힙이 되기 위해서 정렬
		// 루트 노드가 아닐 때만 진행 (즉, 첫 삽입 시에는 정렬 필요 X)
		int idx = size;
		while (idx != 1) {
			// 부모 노드보다 수가 크면 swap
			if (heap[idx] > heap[idx / 2]) {
				heap[idx] = heap[idx / 2];
				heap[idx / 2] = num;
				idx /= 2;
			}
			// 부모 노드보다 작으면 break
			else {
				break;
			}
		}
	}

	static int del() {
		// 힙이 비어있으면 -1 리턴
		if (size == 0) {
			return -1;
		}

		// 그렇지 않으면 루트 노드 리턴
		else {
			int result = heap[1];

			// 마지막 노드를 루트 노드로 변경
			heap[1] = heap[size];
			heap[size] = 0;
			size--;

			// 최대 힙으로 정렬
			// 단말 노드가 되면 break
			int i = 1;
			while (i * 2 <= size + 1) {
				// 왼쪽 자식 노드와 오른쪽 자식 노드 중 큰 노드의 인덱스
				int max_idx = Math.max(heap[i * 2], heap[i * 2 + 1]) == heap[i * 2] ? i * 2 : i * 2 + 1;

				// 자식 노드와 비교하여 자식 노드가 더 크면 swap
				if (heap[i] < heap[max_idx]) {
					int tmp = heap[i];
					heap[i] = heap[max_idx];
					heap[max_idx] = tmp;
					i = max_idx;
				}

				// 아니면 break
				else {
					break;
				}
			}

			return result;
		}
	}
}
