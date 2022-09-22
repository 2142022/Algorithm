import java.util.Scanner;

public class 숫자를정렬하자_퀵정렬_Hoare {
	static int[] nums;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 숫자의 개수
			int N = sc.nextInt();

			// N개의 숫자
			nums = new int[N];
			for (int i = 0; i < N; i++) {
				nums[i] = sc.nextInt();
			}

			// 퀵 정렬 - Hoare
			quickSortHoare(0, N - 1);

			// 출력
			StringBuilder sb = new StringBuilder();
			sb.append("#").append(t);
			for (int i = 0; i < N; i++) {
				sb.append(" ").append(nums[i]);
			}
			System.out.println(sb);
		}
	}

	private static void quickSortHoare(int left, int right) {
		// left >= right가 되면 끝
		if (left >= right) {
			return;
		}

		// 이전 정렬을 통해 pivot의 인덱스를 구할 수 있음
		// pivot을 기준으로 왼쪽과 오른쪽을 분할하여 다시 정렬 (pivot은 정렬이 된 상태)
		int pivot = partition(left, right);
		quickSortHoare(left, pivot - 1);
		quickSortHoare(pivot + 1, right);
	}

	private static int partition(int left, int right) {
		// pivot은 가장 왼쪽 원소
		int pivot = left;

		// L은 왼쪽에서부터 오른쪽으로, R은 오른쪽에서 왼쪽으로 이동
		int L = left + 1;
		int R = right;

		// L <= R일 때까지만 이동
		while (L <= R) {
			// pivot보다 큰 값이 나올 때까지 L 이동
			while ((L <= R) && (nums[L] <= nums[pivot])) {
				L++;
			}

			// pivot보다 작은 값이 나올 때까지 R 이동
			while (nums[R] > nums[pivot]) {
				R--;
			}

			// L과 R의 값 swap
			if (L < R) {
				int tmp = nums[L];
				nums[L] = nums[R];
				nums[R] = tmp;
			}
		}

		// pivot과 R 바꾸기
		int tmp = nums[pivot];
		nums[pivot] = nums[R];
		nums[R] = tmp;

		return R;
	}
}
