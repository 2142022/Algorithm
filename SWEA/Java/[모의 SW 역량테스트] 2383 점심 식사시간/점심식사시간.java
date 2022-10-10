import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class 점심식사시간 {

	// 사람의 수
	static int total;

	// 사람의 위치
	static List<int[]> people;

	// 계단 위치 및 계단 길이
	static List<int[]> stair;

	// 이동 완료 최소 시간
	static int min;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 방의 한 변의 길이
			int N = sc.nextInt();

			// 사람의 수
			total = 0;

			// 사람의 위치
			people = new ArrayList<>();

			// 계단 위치 및 계단 길이
			stair = new ArrayList<>();

			// N X N 지도
			int[][] map = new int[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					map[i][j] = sc.nextInt();

					if (map[i][j] == 1) {
						total++;
						int[] tmp = { i, j };
						people.add(tmp);
					} else if (map[i][j] > 1) {
						int[] tmp = { i, j, map[i][j] };
						stair.add(tmp);
					}
				}
			}

			// 이동 완료 최소 시간
			min = Integer.MAX_VALUE;

			// 계단1을 선택한 사람들이 계단입구까지 이동한 시간 + 대기시간 1분
			List<Integer> choose1 = new ArrayList<>();

			// 계단2을 선택한 사람들이 계단입구까지 이동한 시간 + 대기시간 1분
			List<Integer> choose2 = new ArrayList<>();

			// 한 명씩 계단1, 계단2 중 선택하기
			select(0, choose1, choose2);

			System.out.printf("#%d %d\n", t, min);
		}
	}

	// idx번째 사람이 계단 선택하기
	private static void select(int idx, List<Integer> choose1, List<Integer> choose2) {
		// 모든 사람이 계단을 선택하면 이동 완료 시간 계산하기
		if (idx == total) {
			// choose1, choose2 복사
			List<Integer> cp1 = new ArrayList<>();
			cp1.addAll(choose1);
			List<Integer> cp2 = new ArrayList<>();
			cp2.addAll(choose2);

			// 가까이 있는 사람들부터 계단에 도착하므로 오름차순 정렬
			Collections.sort(cp1);
			Collections.sort(cp2);

			// i초에 계단1 위에 있는 사람들
			int[] stair1 = new int[200];
			for (int i = 0; i < cp1.size(); i++) {
				// i번째 사람이 계단 입구에 도착하여 1분 대기완료한 시간
				int start = cp1.get(i);

				int j = 0;
				while (j != stair.get(0)[2]) {
					// 계단 위에 3명 미만으로 있는 경우
					if (stair1[start + j] < 3) {
						stair1[start + j]++;
						j++;
					} else {
						start++;
						continue;
					}
				}
			}

			// i초에 계단2 위에 있는 사람들
			int[] stair2 = new int[200];
			for (int i = 0; i < cp2.size(); i++) {
				// i번째 사람이 계단 입구에 도착하여 1분 대기완료한 시간
				int start = cp2.get(i);

				int j = 0;
				while (j != stair.get(1)[2]) {
					// 계단 위에 3명 미만으로 있는 경우
					if (stair2[start + j] < 3) {
						stair2[start + j]++;
						j++;
					} else {
						start++;
						continue;
					}
				}
			}

			// 계단1 위에서 마지막 사람이 내려온 시간
			int end1 = 199;
			while (end1 >= 0 && stair1[end1] == 0) {
				end1--;
			}

			// 계단2 위에서 마지막 사람이 내려온 시간
			int end2 = 199;
			while (end2 >= 0 && stair2[end2] == 0) {
				end2--;
			}

			min = Math.min(min, Math.max(end1, end2) + 1);
			return;
		}

		// 계단1까지와의 거리 + 대기시간 1분
		int dist = Math.abs(people.get(idx)[0] - stair.get(0)[0]) + Math.abs(people.get(idx)[1] - stair.get(0)[1]) + 1;

		// 계단1을 선택하는 경우
		choose1.add(dist);
		select(idx + 1, choose1, choose2);

		// 원상태 복귀
		choose1.remove(choose1.size() - 1);

		// 계단2까지의와의 거리 + 대기시간 1분
		dist = Math.abs(people.get(idx)[0] - stair.get(1)[0]) + Math.abs(people.get(idx)[1] - stair.get(1)[1]) + 1;

		// 계단2을 선택하는 경우
		choose2.add(dist);
		select(idx + 1, choose1, choose2);

		// 원상태 복귀
		choose2.remove(choose2.size() - 1);
	}
}
