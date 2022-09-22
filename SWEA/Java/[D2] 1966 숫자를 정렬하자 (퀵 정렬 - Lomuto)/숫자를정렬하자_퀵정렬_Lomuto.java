import java.util.Scanner;

public class 숫자를정렬하자_퀵정렬_Lomuto {
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

			// 퀵 정렬 - Lomuto
			quickSortLomuto(0, N - 1);

			// 출력
			StringBuilder sb = new StringBuilder();
			sb.append("#").append(t);
			for (int i = 0; i < N; i++) {
				sb.append(" ").append(nums[i]);
			}
			System.out.println(sb);
		}
	}

	private static void quickSortLomuto(int left, int right) {
		// left >= right가 되면 끝
		if (left >= right) {
			return;
		}

		// 이전 정렬을 통해 pivot의 인덱스를 구할 수 있음
		// pivot을 기준으로 왼쪽과 오른쪽을 분할하여 다시 정렬 (pivot은 정렬이 된 상태)
		int pivot = partition(left, right);
		quickSortLomuto(left, pivot - 1);
		quickSortLomuto(pivot + 1, right);
	}

	private static int partition(int left, int right) {
		// pivot은 가장 오른쪽
		int pivot = right;
		// pivot보다 작은 값들의 경계
		int i = left - 1;

		// pivot보다 작은 값들을 왼쪽으로, 큰 값들을 오른쪽으로
		for (int j = left; j < right; j++) {
			if (nums[j] <= nums[pivot]) {
				i++;
				swap(i, j);
			}
		}

		// pivot을 기준으로 작은 값들과 큰 값들로 나눠졌으므로 pivot의 위치를 구할 수 있음
		swap(i + 1, pivot);

		return i + 1;
	}

	private static void swap(int i, int j) {
		int tmp = nums[i];
		nums[i] = nums[j];
		nums[j] = tmp;
	}
}
