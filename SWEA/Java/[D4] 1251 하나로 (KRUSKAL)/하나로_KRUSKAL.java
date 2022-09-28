import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class 하나로_KRUSKAL {

	// 대표를 저장할 배열
	static int[] p;

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

			// 섬들끼리 연결했을 때 나오는 모든 해저터널
			// 해저터널의 개수: N * (N - 1) / 2
			int S = N * (N - 1) / 2;
			double[][] tunnel = new double[S][3];
			int idx = 0;

			for (int i = 0; i < N; i++) {
				for (int j = i + 1; j < N; j++) {
					// i번째 섬에서 시작
					tunnel[idx][0] = i;

					// j번째 섬에 도착
					tunnel[idx][1] = j;

					// i번째 섬과 j번째 섬 사이 거리의 제곱
					tunnel[idx][2] = Math.pow(island[i][0] - island[j][0], 2)
							+ Math.pow(island[i][1] - island[j][1], 2);
					idx++;
				}
			}

			// 거리 기준으로 오름차순 정렬
			Arrays.sort(tunnel, new Comparator<double[]>() {
				@Override
				public int compare(double[] o1, double[] o2) {
					return (int) (o1[2] - o2[2]);
				}
			});

			// 대표를 저장할 배열
			p = new int[N];

			// make-set: 자기 자신을 대표로 초기화
			for (int i = 0; i < N; i++) {
				p[i] = i;
			}

			// 연결된 해저터널의 총 길이의 최소
			double min = 0;

			// 연결된 해저터널의 개수
			int cnt = 0;

			for (int i = 0; i < S; i++) {
				// 해저터널을 총 N - 1개 연결됐다면 끝내기
				if (cnt == (N - 1)) {
					break;
				}

				// i번째 해저터널을 뽑아서 두 섬의 대표 확인
				// 대표가 같다면 pass, 다르다면 union
				int px = findSet(tunnel[i][0]);
				int py = findSet(tunnel[i][1]);

				if (px != py) {
					union(px, py);
					cnt++;
					min += tunnel[i][2];
				}
			}

			// 환경 부담 세율 실수 E
			double E = sc.nextDouble();

			System.out.printf("#%d %d\n", t, Math.round(min * E));
		}
	}

	private static int findSet(double x) {
		// Path Compression
		if ((int) x != p[(int) x]) {
			p[(int) x] = findSet(p[(int) x]);
		}
		return p[(int) x];
	}

	private static void union(int x, int y) {
		p[y] = x;
	}
}
