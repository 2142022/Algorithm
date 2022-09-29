import java.util.Scanner;

public class 창용마을무리의개수 {
	// 부모 저장 (무리의 대표)
	static int[] p;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 마을 인구 수
			int N = sc.nextInt();

			// 사람들의 관계 수
			int M = sc.nextInt();

			// 관계 정보
			int[][] relation = new int[M][2];
			for (int i = 0; i < M; i++) {
				relation[i][0] = sc.nextInt();
				relation[i][1] = sc.nextInt();
			}

			// 총 무리의 개수 (인구수로 초기화)
			int group = N;

			// 부모 저장 (무리의 대표)
			p = new int[N + 1];

			// make-set: 모든 사람들을 대표로 초기화
			for (int i = 1; i < N + 1; i++) {
				p[i] = i;
			}

			// 관계 있는 사람들이 포함된 무리의 대표자 확인
			for (int i = 0; i < M; i++) {
				// 대표자 찾기
				int p1 = findSet(relation[i][0]);
				int p2 = findSet(relation[i][1]);

				// 대표가 같다면 pass, 다르다면 union을 통해 무리 합치기
				if (p1 != p2) {
					union(p1, p2);

					// 총 무리의 개수는 1개 감소
					group--;
				}
			}

			System.out.printf("#%d %d\n", t, group);
		}
	}

	// 무리의 대표 찾기
	private static int findSet(int pNum) {
		// pNum이 대표자가 아니라면 무리의 대표 저장하고 반환
		if (pNum != p[pNum]) {
			p[pNum] = findSet(p[pNum]);
		}

		return p[pNum];
	}

	private static void union(int p1, int p2) {
		p[p2] = p1;
	}
}
