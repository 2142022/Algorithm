import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class 무선충전 {
	// BC의 개수
	static int A;

	// BC의 정보
	static int[][] BC;

	// 사용자 A의 이동 정보
	static int[] dirA;

	// 사용자 B의 이동 정보
	static int[] dirB;

	// 사용자 A의 위치
	static int AX;
	static int AY;

	// 사용자 B의 위치
	static int BX;
	static int BY;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 총 이동시간 (0일 때도 포함해야 하므로 +1)
			int M = sc.nextInt() + 1;

			// BC의 개수
			A = sc.nextInt();

			// 사용자 A의 이동 정보
			dirA = new int[M];
			for (int i = 1; i < M; i++) {
				dirA[i] = sc.nextInt();
			}

			// 사용자 B의 이동 정보
			dirB = new int[M];
			for (int i = 1; i < M; i++) {
				dirB[i] = sc.nextInt();
			}

			// BC의 정보
			BC = new int[A][4];
			for (int i = 0; i < A; i++) {
				// BC의 위치 (주의: (y, x)로 입력됨)
				BC[i][1] = sc.nextInt();
				BC[i][0] = sc.nextInt();

				// BC의 충전 범위
				BC[i][2] = sc.nextInt();

				// BC의 성능
				BC[i][3] = sc.nextInt();
			}

			// 모든 사용자의 충전량 합의 최대값
			int max = 0;

			// 초마다 충전량의 합 구하기
			for (int i = 0; i < M; i++) {
				// 사용자 A의 위치 구하기
				getPos(i, AX, AY, 'A');

				// 사용자 B의 위치 구하기
				getPos(i, BX, BY, 'B');

				// 현재 사용자 A가 사용 가능한 BC의 번호
				List<Integer> useA = getBC(AX, AY);

				// 현재 사용자 B가 사용 가능한 BC의 번호
				List<Integer> useB = getBC(BX, BY);

				// 사용자 A가 최대 성능을 가진 BC를 선택한 경우의 충전량 합
				int result1 = charge(useA, useB);

				// 사용자 B가 최대 성능을 가진 BC를 선택한 경우의 충전량 합
				int result2 = charge(useB, useA);

				max += Math.max(result1, result2);
			}

			System.out.printf("#%d %d\n", t, max);
		}
	}

	// 사용자 1이 최대 성능을 가진 BC를 선택한 경우의 충전량 합
	private static int charge(List<Integer> use1, List<Integer> use2) {
		// 사용자1의 최대 충전량
		int charge1 = 0;
		// 사용자1의 최대 충전량일 때의 BC 번호
		int idx1 = -1;
		// 사용자2의 최대 충전량
		int charge2 = 0;
		// 사용자2의 최대 충전량일 때의 BC 번호
		int idx2 = -1;

		// 사용자1이 사용할 수 있는 BC가 없는 경우
		if (use1.size() == 0) {
			charge1 = 0;
			idx1 = -1;

			// 사용자2가 사용할 수 있는 BC가 없는 경우
			if (use2.size() == 0) {
				charge2 = 0;
				idx2 = -1;
			}

			// 사용자2의 최대 성능 BC 정하기
			else {
				for (int i = 0; i < use2.size(); i++) {
					// BC 번호
					int idx = use2.get(i);

					// 현재 BC의 성능이 기존 최대 성능보다 큰 경우 charge2 바꾸기
					if (BC[idx][3] > charge2) {
						charge2 = BC[idx][3];
						idx2 = idx;
					}
				}
			}
		}

		// 사용자1의 최대 성능 BC 구하기
		else {
			for (int i = 0; i < use1.size(); i++) {
				// BC 번호
				int idx = use1.get(i);

				// 현재 BC의 성능이 기존 최대 성능보다 큰 경우 charge1 바꾸기
				if (BC[idx][3] > charge1) {
					charge1 = BC[idx][3];
					idx1 = idx;
				}
			}

			// 사용자2가 사용할 수 있는 BC가 없는 경우
			if (use2.size() == 0) {
				charge2 = 0;
				idx2 = -1;
			}

			// 사용자2가 사용할 수 있는 BC가 1개인 경우
			else if (use2.size() == 1) {
				idx2 = use2.get(0);

				// 사용자2가 사용할 수 있는 BC가 사용자1이 선택한 BC인 경우
				if (idx1 == idx2) {
					charge1 /= 2;
					charge2 = charge1;
				}

				// 사용자2가 사용할 수 있는 BC가 사용자1이 선택한 BC가 아닌 경우
				else {
					charge2 = BC[idx2][3];
				}
			}

			// 사용자2가 사용할 수 있는 BC가 2개인 이상인 경우
			// 사용자1이 선택한 BC를 제외하고 최대 성능 BC 고르기
			else {
				for (int i = 0; i < use2.size(); i++) {
					int idx = use2.get(i);

					if ((idx != idx1) && (BC[idx][3] > charge2)) {
						charge2 = BC[idx][3];
						idx2 = idx;
					}
				}
			}
		}

		return charge1 + charge2;
	}

	// 사용자가 (x, y)에 있을 때 사용 가능한 BC 구하기
	private static List<Integer> getBC(int x, int y) {
		List<Integer> result = new ArrayList<>();

		// 각각의 BC가 사용 가능한지 확인
		for (int i = 0; i < A; i++) {
			if (Math.abs(BC[i][0] - x) + Math.abs(BC[i][1] - y) <= BC[i][2]) {
				result.add(i);
			}
		}

		return result;
	}

	// 사용자의 위치 구하기
	private static void getPos(int idx, int x, int y, char c) {
		if (idx == 0) {
			x = (c == 'A') ? 1 : 10;
			y = (c == 'A') ? 1 : 10;
		} else {
			int dir = (c == 'A') ? dirA[idx] : dirB[idx];
			switch (dir) {
			// 위로 이동
			case 1:
				x--;
				break;
			// 오른쪽으로 이동
			case 2:
				y++;
				break;
			// 아래로 이동
			case 3:
				x++;
				break;
			// 왼쪽으로 이동
			case 4:
				y--;
				break;
			}
		}

		if (c == 'A') {
			AX = x;
			AY = y;
		} else {
			BX = x;
			BY = y;
		}
	}
}
