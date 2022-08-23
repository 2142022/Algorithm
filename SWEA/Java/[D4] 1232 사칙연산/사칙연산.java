import java.util.Scanner;

public class 사칙연산 {
	// 노드 정보 입력받기: 노드 번호, 연산자(두 개의 피연산자 노드 번호) / 피연산자
	static int[][] node;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 10개의 테스트케이스
		for (int t = 1; t <= 10; t++) {
			// 노드 개수
			int N = sc.nextInt();

			// 노드 정보 입력받기: 노드 번호, 연산자(두 개의 피연산자 노드 번호) / 피연산자
			node = new int[N + 1][3];

			for (int i = 0; i < N; i++) {
				// 노드의 번호
				int idx = sc.nextInt();

				// 연산자인지 피연산자인지 구분하기 위해 string으로 입력받기
				String tmp = sc.next();

				// +: -1, -: -2, *: -3, /: -4
				if (tmp.equals("+")) {
					node[idx][0] = -1;
					node[idx][1] = sc.nextInt();
					node[idx][2] = sc.nextInt();
				} else if (tmp.equals("-")) {
					node[idx][0] = -2;
					node[idx][1] = sc.nextInt();
					node[idx][2] = sc.nextInt();
				} else if (tmp.equals("*")) {
					node[idx][0] = -3;
					node[idx][1] = sc.nextInt();
					node[idx][2] = sc.nextInt();
				} else if (tmp.equals("/")) {
					node[idx][0] = -4;
					node[idx][1] = sc.nextInt();
					node[idx][2] = sc.nextInt();
				} else {
					// 피연산자라면 입력받은 문자열을 int로 바꿔서 저장
					node[idx][0] = Integer.parseInt(tmp);
				}
			}

			// 재귀함수를 통해서 계산
			System.out.printf("#%d %d\n", t, cal(1));
		}
	}

	// 트리 계산 (매개변수는 node의 인덱스)
	static int cal(int i) {
		double result = 0;

		// node가 연산자 +일 때
		if (node[i][0] == -1) {
			result = cal(node[i][1]) + cal(node[i][2]);
		}

		// node가 연산자 -일 때
		else if (node[i][0] == -2) {
			result = cal(node[i][1]) - cal(node[i][2]);
		}

		// node가 연산자 *일 때
		else if (node[i][0] == -3) {
			result = cal(node[i][1]) * cal(node[i][2]);
		}

		// node가 연산자 /일 때
		else if (node[i][0] == -4) {
			result = cal(node[i][1]) / cal(node[i][2]);
		}

		// 그 외에는 피연산자이므로 리턴
		else {
			return node[i][0];
		}

		return (int) result;
	}
}
