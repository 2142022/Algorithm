import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

public class 하나로_Prim_우선순위큐 {
	// 터널 정보를 나타내는 클래스
	static class Tunnel implements Comparable<Tunnel> {
		// 터널의 시작(섬), 터널의 끝(섬), 터널의 길이의 제곱(섬과 섬 사이의 거리의 제곱)
		int st;
		int ed;
		double len;

		public Tunnel(int st, int ed, double len) {
			this.st = st;
			this.ed = ed;
			this.len = len;
		}

		@Override
		public int compareTo(Tunnel o) {
			// 최소 힙
			return (int) (this.len - o.len);
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 섬의 개수
			int N = sc.nextInt();

			// 각 섬들의 좌표
			int[][] island = new int[N][2];

			// X좌표
			for (int i = 0; i < N; i++) {
				island[i][0] = sc.nextInt();
			}

			// Y좌표
			for (int i = 0; i < N; i++) {
				island[i][1] = sc.nextInt();
			}

			// 인접 리스트
			// 모든 해저터널의 정보 입력하기
			List<Tunnel>[] adjList = new ArrayList[N];
			for (int i = 0; i < N; i++) {
				adjList[i] = new ArrayList<>();
				for (int j = 0; j < N; j++) {
					double tmp = Math.pow(island[i][0] - island[j][0], 2) + Math.pow(island[i][1] - island[j][1], 2);
					adjList[i].add(new Tunnel(i, j, tmp));
				}
			}

			// 방문 체크
			int[] visit = new int[N];

			// 우선순위 큐
			// 현재 섬에 연결된 가장 짧은 해저터널을 바로 뽑아낼 수 있음
			PriorityQueue<Tunnel> pq = new PriorityQueue<>();

			// 0번째 섬부터 시작 (다른 섬부터 해도 상관 없음)
			visit[0] = 1;
			// 0번째 섬에 연결된 모든 해저터널의 정보를 추가
			pq.addAll(adjList[0]);

			// 이미 확보한 섬의 개수
			int cnt = 1;
			// 최소 거리의 합
			double result = 0;

			// 마지막 섬은 더 이상 연결될 해저터널이 없으므로 확인하지 않아도 됨
			while (cnt < N) {
				// 연결된 가장 짧은 해저터널 뽑기
				Tunnel tunnel = pq.poll();

				// 이미 방문한 섬은 pass
				if (visit[tunnel.ed] == 1) {
					continue;
				}

				result += tunnel.len;
				pq.addAll(adjList[tunnel.ed]);
				visit[tunnel.ed] = 1;
				cnt++;
			}

			// 환경 부담 세율 실수 E
			double E = sc.nextDouble();

			System.out.printf("#%d %d\n", t, Math.round(result * E));
		}
	}
}
