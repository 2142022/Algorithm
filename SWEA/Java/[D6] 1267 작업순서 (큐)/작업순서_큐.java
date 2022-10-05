import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class 작업순서_큐 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 10개의 테스트케이스
		for (int t = 1; t <= 10; t++) {
			StringBuilder sb = new StringBuilder();
			sb.append("#").append(t);

			// 정점의 개수
			int V = sc.nextInt();

			// 간선의 개수
			int E = sc.nextInt();

			// 진입차수 (i번째 정점으로 들어오는 간선의 개수)
			int[] indegree = new int[V + 1];

			// 인접리스트 (간선의 정보)
			List<Integer>[] edge = new ArrayList[V + 1];
			for (int i = 0; i < E; i++) {
				int start = sc.nextInt();
				int end = sc.nextInt();

				if (edge[start] == null) {
					edge[start] = new ArrayList<>();
				}

				edge[start].add(end);
				indegree[end]++;
			}

			Queue<Integer> queue = new LinkedList<>();

			// 진입차수가 0인 정점들 큐에 넣기
			for (int i = 1; i < V + 1; i++) {
				if (indegree[i] == 0) {
					queue.offer(i);
				}
			}

			// 큐의 원소가 없어질 때까지 반복
			while (!queue.isEmpty()) {
				// 원소 뽑기
				int now = queue.poll();
				sb.append(" ").append(now);

				// 현재 원소 다음으로 갈 수 있는 정점 찾기
				if (edge[now] != null) {
					for (int i = 0; i < edge[now].size(); i++) {
						// 연결된 정점
						int next = edge[now].get(i);

						// 진입차수 1개 줄이기
						indegree[next]--;

						// 진입차수가 0이 되었다면 큐에 넣기
						if (indegree[next] == 0) {
							queue.offer(next);
						}
					}
				}
			}

			System.out.println(sb);
		}
	}
}
