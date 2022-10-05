import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;

public class 작업순서_스택 {
	// 인접리스트 (간선의 정보)
	static List<Integer>[] edge;

	// 방문 체크
	static int[] visit;

	// 결과 (스택)
	static Stack<Integer> result;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 10개의 테스트케이스
		for (int t = 1; t <= 10; t++) {
			// 정점의 개수
			int V = sc.nextInt();

			// 간선의 개수
			int E = sc.nextInt();

			// 진입차수 (i번째 정점으로 들어오는 간선의 개수)
			int[] indegree = new int[V + 1];

			// 인접리스트 (간선의 정보)
			edge = new ArrayList[V + 1];
			for (int i = 0; i < E; i++) {
				int start = sc.nextInt();
				int end = sc.nextInt();

				if (edge[start] == null) {
					edge[start] = new ArrayList<>();
				}

				edge[start].add(end);
				indegree[end]++;
			}

			// 방문 체크
			visit = new int[V + 1];

			// 결과 (스택)
			result = new Stack<>();

			// 진입 차수가 0인 정점부터 dfs로 스택에 넣기
			for (int i = 1; i < V + 1; i++) {
				if (indegree[i] == 0) {
					dfs(i);
				}
			}

			// 출력
			System.out.print("#" + t);
			while (!result.isEmpty()) {
				// 스택 하나씩 꺼내기
				System.out.print(" " + result.pop());
			}
			System.out.println();
		}
	}

	private static void dfs(int num) {
		// 방문 체크
		visit[num] = 1;

		// 재귀로 다음 노드 구하기
		if (edge[num] != null) {
			for (int i = 0; i < edge[num].size(); i++) {
				// 다음 노드
				int next = edge[num].get(i);

				// 아직 방문하지 않았다면 재귀
				if (visit[next] == 0) {
					dfs(next);
				}
			}
		}

		// 스택에 넣기 (재귀를 다 돌고 넣으므로 끝 번호부터 넣게 됨)
		result.push(num);
	}
}
