import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class 음악프로그램 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 가수의 수
		int N = sc.nextInt();

		// 보조 PD의 수
		int M = sc.nextInt();

		// 진입차수
		// indegree[i]: 가수 i로 들어올 수 있는 간선의 수
		int[] indegree = new int[N + 1];

		// 인접리스트
		// 각 가수 다음으로 출연할 수 있는 가수
		List<Integer>[] info = new ArrayList[N + 1];
		for (int i = 0; i < M; i++) {
			// 현재 보조 PD가 맡은 가수의 수
			int cnt = sc.nextInt();

			// 현재 보조 PD가 맡은 가수
			int[] singer = new int[cnt];
			for (int j = 0; j < cnt; j++) {
				singer[j] = sc.nextInt();
			}

			// 인접리스트 채우기
			for (int j = 0; j < cnt - 1; j++) {
				if (info[singer[j]] == null) {
					info[singer[j]] = new ArrayList<>();
				}

				info[singer[j]].add(singer[j + 1]);
				indegree[singer[j + 1]]++;
			}
		}

		// 가수들을 출연 순서대로 뽑은 결과
		List<Integer> result = new ArrayList<>();

		// 가수들을 출연 순서대로 뽑기 위해 큐 이용
		Queue<Integer> queue = new LinkedList<>();

		// 진입차수가 0인 가수들 모두 큐에 넣기
		for (int i = 1; i < N + 1; i++) {
			if (indegree[i] == 0) {
				queue.offer(i);
			}
		}

		// 큐가 빌 때까지 반복
		while (!queue.isEmpty()) {
			// 가수 한명 뽑기
			int singer = queue.poll();
			result.add(singer);

			// 현재 가수 다음으로 올 수 있는 가수 찾고 진입차수 낮추기
			if (info[singer] != null) {
				for (int i = 0; i < info[singer].size(); i++) {
					// 현재 가수와 연결된 가수
					int next = info[singer].get(i);
					indegree[next]--;

					// 가수의 진입차수가 0이 되었다면 큐에 추가
					// 진입차수가 0이 될 때 바로 큐에 넣으므로 방문 체크 필요 없음
					if (indegree[next] == 0) {
						queue.offer(next);
					}
				}
			}
		}

		// result의 크기가 전체 가수의 수와 다르다면 전체 가수의 순서를 정할 수 없음
		if (result.size() != N) {
			System.out.println(0);
		} else {
			for (int i = 0; i < result.size(); i++) {
				System.out.println(result.get(i));
			}
		}
	}
}
