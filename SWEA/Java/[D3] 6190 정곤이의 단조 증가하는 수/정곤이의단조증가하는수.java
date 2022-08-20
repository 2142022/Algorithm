import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class 정곤이의단조증가하는수 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 숫자 개수
			int N = sc.nextInt();

			// 숫자 입력받기
			int[] A = new int[N];
			for (int i = 0; i < N; i++) {
				A[i] = sc.nextInt();
			}

			// 단조 증가하는 Ai X Aj 중 최대값 찾기
			int max = -1;
			for (int i = 0; i < N; i++) {
				for (int j = i + 1; j < N; j++) {
					// 단조 증가하는 수라면 최댓값과 비교
					if (check(A[i] * A[j])) {
						max = Math.max(max, A[i] * A[j]);
					}
				}
			}

			// 출력
			System.out.printf("#%d %d\n", t, max);
		}
	}

	// 단조 증가하는 수인지 확인
	static boolean check(int num) {
		// num의 각 자리 숫자를 거꾸로 리스트로 만들기
		List<Integer> list = new ArrayList<>();
		while (num > 0) {
			list.add(num % 10);
			num /= 10;
		}

		// 리스트가 내림차순으로 정렬되어 있으면 단조 증가하는 수
		for (int i = 0; i < list.size() - 1; i++) {
			if (list.get(i) < list.get(i + 1)) {
				return false;
			}
		}

		return true;
	}
}
