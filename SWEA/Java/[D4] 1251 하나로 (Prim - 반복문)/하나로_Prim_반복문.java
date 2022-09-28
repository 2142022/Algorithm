import java.util.Arrays;
import java.util.Scanner;

public class 하나로_Prim_반복문 {
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

			// 인접 행렬
			// i번째 섬과 j번째 섬 사이의 거리의 제곱을 나타내는 배열
			double[][] tunnel = new double[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = i + 1; j < N; j++) {
					tunnel[i][j] = Math.pow(island[i][0] - island[j][0], 2) + Math.pow(island[i][1] - island[j][1], 2);
					tunnel[j][i] = tunnel[i][j];
				}
			}

			// 방문 체크
			int[] visit = new int[N];
			// 값(부모로부터의 최소 거리)을 저장하기 위한 배열
			double[] length = new double[N];
			// 어디서 왔는지 저장하기 위한 배열 (부모정보)
			int[] p = new int[N];

			// length를 최대한 큰 값으로 초기화
			Arrays.fill(length, Double.MAX_VALUE);

			// 0번째 섬부터 시작 (다른 섬부터 해도 상관 없음)
			length[0] = 0;
			p[0] = -1;

			// 마지막 섬에 연결된 섬들은 이미 다 확인했으므로 N - 1까지만 확인해도 됨
			for (int i = 0; i < N - 1; i++) {
				// 해저터널 중 가장 짧은 길이
				double min = Double.MAX_VALUE;

				// 해저터널 중 가장 짧은 길이가 있는 인덱스
				int idx = i;

				// 아직 방문 체크하지 않은 섬들 중 해저터널의 길이가 가장 짧은 것 구하기
				for (int j = 0; j < N; j++) {
					if ((visit[j] == 0) && (length[j] < min)) {
						min = length[j];
						idx = j;
					}
				}

				// 방문체크
				visit[idx] = 1;

				// 위에서 구한 해저터널 정보 갱신하기
				for (int j = 0; j < N; j++) {
					// 아직 방문하지 않았고 현재 저장된 length가 원래 해저터널 길이보다 크다면 값 바꾸기
					if ((visit[j] == 0) && (length[j] > tunnel[idx][j])) {
						length[j] = tunnel[idx][j];
						p[j] = idx;
					}
				}
			}
			// 최소 거리의 합
			double result = 0;
			for (int i = 0; i < N; i++) {
				result += length[i];
			}

			// 환경 부담 세율 실수 E
			double E = sc.nextDouble();

			System.out.printf("#%d %d\n", t, Math.round(result * E));
		}
	}
}
