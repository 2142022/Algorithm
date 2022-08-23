import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class 공통조상 {
	static StringBuilder sb;

	// 노드의 개수
	static int V;

	// 간선의 개수
	static int E;

	// 공통 조상을 찾고 싶은 두 노드 입력받기
	static int n1;
	static int n2;

	// 부모와 자식 관계를 2차 배열로 입력받기
	static int[][] relation;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			sb = new StringBuilder();

			// 노드의 개수
			V = sc.nextInt();

			// 간선의 개수
			E = sc.nextInt();

			// 공통 조상을 찾고 싶은 두 노드 입력받기
			n1 = sc.nextInt();
			n2 = sc.nextInt();

			// 부모와 자식 관계를 2차 배열로 입력받기
			relation = new int[E][2];
			for (int i = 0; i < E; i++) {
				relation[i][0] = sc.nextInt();
				relation[i][1] = sc.nextInt();
			}

			// n1부터 루트 노드까지의 리스트
			List<Integer> n1List = getList(n1);

			// n2부터 루트 노드까지의 리스트
			List<Integer> n2List = getList(n2);

			// 루트 노드부터 공통 조상의 개수 확인
			int i = 1;
			while (n1List.get(n1List.size() - 1 - i).equals(n2List.get(n2List.size() - 1 - i))) {
				i++;
			}

			// 공통 조상의 개수: i개
			// 가장 가까운 공통 조상
			int common = n1List.get(n1List.size() - i);
			sb.append("#" + t + " " + common + " ");

			// 가장 가까운 공통 조상을 루트 노드로 하는 서브 트리의 크기: 노드 개수 구하기
			// 노드의 개수
			int size = 1;
			size = count(common, size);
			sb.append(size);

			System.out.println(sb);
		}
	}

	// 노드부터 루트 노드까지의 리스트 구하기
	static List<Integer> getList(int n) {
		List<Integer> result = new ArrayList<>();
		result.add(n);

		while (n != 1) {
			for (int i = 0; i < E; i++) {
				// 자식노드가 n이라면 n의 부모노드를 add
				if (relation[i][1] == n) {
					result.add(relation[i][0]);
					n = relation[i][0];
					break;
				}
			}
		}

		return result;
	}

	// 트리의 크기 구하기
	static int count(int n, int cnt) {
		// 자식 노드가 있으면 1, 없으면 0
		int flag = 0;

		for (int i = 0; i < E; i++) {
			if (relation[i][0] == n) {
				flag = 1;
			}
		}

		// 자식 노드가 있으면 재귀
		if (flag == 1) {
			for (int i = 0; i < E; i++) {
				if (relation[i][0] == n) {
					cnt++;
					cnt = count(relation[i][1], cnt);
				}
			}
			return cnt;
		}

		return cnt;
	}
}
