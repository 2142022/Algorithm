import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class 줄세우기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();

		// 학생 수
		int N = sc.nextInt();

		// 학생 비교 횟수
		int M = sc.nextInt();

		// 진입차수
		// indegree[i]: 학생 i로 들어오는 간선의 수
		int[] indegree = new int[N + 1];

		// 인접 리스트
		// info[A] = B: 학생 A가 학생 B 앞에 있어야 함
		List<Integer>[] info = new ArrayList[N + 1];
		for (int i = 0; i < M; i++) {
			int A = sc.nextInt();
			int B = sc.nextInt();

			if (info[A] == null) {
				info[A] = new ArrayList<>();
			}

			info[A].add(B);
			indegree[B]++;
		}

		// 연결된 학생들을 순서대로 찾기 위해 큐 이용
		Queue<Integer> queue = new LinkedList<>();

		// 진입차수가 0인 학생들을 모두 큐에 넣기
		for (int i = 1; i < N + 1; i++) {
			if (indegree[i] == 0) {
				queue.offer(i);
			}
		}

		// 큐의 원소가 빌 때까지 반복
		while (!queue.isEmpty()) {
			// 큐에서 학생 뽑기
			int student = queue.poll();
			sb.append(student).append(" ");

			// 현재 학생과 연결된 학생을 찾고 진입차수 감소시키기
			if (info[student] != null) {
				for (int i = 0; i < info[student].size(); i++) {
					int next = info[student].get(i);
					indegree[next]--;

					// 연결된 학생의 진입차수가 0이 되었다면 큐에 넣기
					// 진입차수가 0이 되면 바로 큐에 넣으므로 방문 체크를 할 필요가 없음
					if (indegree[next] == 0) {
						queue.offer(next);
					}
				}
			}
		}

		System.out.println(sb);
	}
}
