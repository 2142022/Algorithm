import java.util.Scanner;

public class 디저트카페 {

	// 지역 크기
	static int N;

	// 디저트 카페 정보
	static int[][] dessert;

	// 가장 많이 먹을 때의 디저트 수
	static int max;

	// 먹은 디저트 종류
	static int[] eat;

	// 이동 칸 수
	static int[] move;

	// 델타
	static int[] dr = { 1, 1, -1, -1 };
	static int[] dc = { 1, -1, -1, 1 };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 지역 크기
			N = sc.nextInt();

			// 디저트 카페 정보
			dessert = new int[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					dessert[i][j] = sc.nextInt();
				}
			}

			// 먹은 디저트 종류
			eat = new int[101];

			// 가장 많이 먹을 때의 디저트 수
			max = -1;

			// 출발 위치 선정
			for (int i = 0; i < N - 2; i++) {
				for (int j = 1; j < N - 1; j++) {
					// 이동 칸 수
					// 0: 오른쪽 하단으로 이동한 칸 수
					// 1: 왼쪽 하단으로 이동한 칸 수
					// 2: 왼쪽 상단으로 이동한 칸 수
					// 3: 오른쪽 상단으로 이동한 칸 수
					move = new int[4];
					tour(i, j, 0);
				}
			}

			System.out.printf("#%d %d\n", t, max);
		}
	}

	// 인자: 현재 위치(r, c), 방향
	private static void tour(int r, int c, int dir) {
		// 방향을 3번 다 바꾸면 끝내기
		if (dir == 4) {
			// 평행한 변의 길이가 같아야 함 (이동 칸 수가 같아야 함)
			// 무조건 한 칸 이상은 이동해야 함
			if ((move[0] == move[2]) && (move[1] == move[3]) && (move[0] > 0) && (move[1] > 0)) {
				max = Math.max(max, move[0] + move[1] + move[2] + move[3]);
			}

			return;
		}

		// 다음 위치
		int nextR = r + dr[dir];
		int nextC = c + dc[dir];

		// 다음 위치에 갈 수 있으면 가기 (인덱스 범위안에 있고, 해당 디저트를 먹지 않았을 때)
		if ((nextR >= 0) && (nextR < N) && (nextC >= 0) && (nextC < N) && (eat[dessert[nextR][nextC]] == 0)) {
			// 방문 체크
			eat[dessert[nextR][nextC]] = 1;

			// 이동 횟수 추가
			move[dir]++;

			// 위치 이동
			tour(nextR, nextC, dir);

			// 돌아온 후에는 이동 횟수 감소, 방문 체크 취소
			move[dir]--;
			eat[dessert[nextR][nextC]] = 0;
		}

		// 방향 바꾸기
		tour(r, c, dir + 1);
	}
}
