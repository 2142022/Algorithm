import java.util.Scanner;

public class 중위순회 {
	static StringBuilder sb;

	// 노드의 개수
	static int N;

	// 트리
	static char[] tree;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 10개의 테스트케이스
		for (int t = 1; t <= 10; t++) {
			// 노드의 개수
			N = sc.nextInt();

			// 노드 정보 입력받아서 트리 만들기
			// 노드 정보는 완전 이진 트리 순서 그대로 입력됨
			tree = new char[N + 1];
			for (int i = 1; i <= N; i++) {
				// 어차피 완전 이진 트리 순서 그대로 입력되므로 노드 번호 필요없음
				// 노드 번호 입력받고 버림
				sc.next();

				// 노드의 알파벳
				tree[i] = sc.next().charAt(0);

				// 어차피 완전 이진 트리 순서 그대로 입력되므로 자식 노드 번호 필요없음
				// 자식 노드가 있다면 입력받고 버림
				// 왼쪽 자식 노드가 있을 때
				if (i * 2 <= N) {
					sc.next();
				}

				// 오른쪽 자식 노드가 있을 때
				if (i * 2 + 1 <= N) {
					sc.next();
				}
			}

			sb = new StringBuilder();
			sb.append("#" + t + " ");

			// 중위순회
			inOrder(1);

			System.out.println(sb);
		}
	}

	// 중위순회 (인자는 부모 노드의 인덱스)
	static void inOrder(int i) {
		// 재귀로 왼쪽 자식노드 구하기
		if (i * 2 <= N) {
			inOrder(i * 2);
		}

		// 부모노드
		sb.append(tree[i]);

		// 재귀로 오른쪽 자식노드
		if (i * 2 + 1 <= N) {
			inOrder(i * 2 + 1);
		}
	}
}