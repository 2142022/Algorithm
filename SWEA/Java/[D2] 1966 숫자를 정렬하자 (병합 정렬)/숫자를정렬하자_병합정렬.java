import java.util.Scanner;

public class 숫자를정렬하자_병합정렬 {
	// 숫자의 개수
	static int N;

	// 정렬 전 숫자
	static int[] nums;

	// 정렬 후 숫자
	static int[] result;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 숫자의 개수
			N = sc.nextInt();

			// N개의 숫자
			nums = new int[N];
			for (int i = 0; i < N; i++) {
				nums[i] = sc.nextInt();
			}

			// 정렬 후 숫자
			result = new int[N];

			// 병합 정렬(왼쪽 인덱스, 오른쪽 인덱스)
			mergeSort(0, N - 1);

			// 출력
			StringBuilder sb = new StringBuilder();
			sb.append("#").append(t);
			for (int i = 0; i < N; i++) {
				sb.append(" ").append(nums[i]);
			}
			System.out.println(sb);
		}
	}

	private static void mergeSort(int left, int right) {
		// left >= right면 분할 끝
		if (left >= right) {
			return;
		}

		// left와 right의 중간 인덱스
		int mid = (left + right) / 2;

		// 왼쪽 분할
		mergeSort(left, mid);

		// 오른쪽 분할
		mergeSort(mid + 1, right);

		// 분할된 집합 병합
		merge(left, mid, right);
	}

	private static void merge(int left, int mid, int right) {
		// 왼쪽 구간 시작 인덱스
		int L = left;
		// 오른쪽 구간 시작 인덱스
		int R = mid + 1;
		// 정렬된 원소 삽입 위치
		int idx = left;

		// 왼쪽 분할, 오른쪽 분할 모두 값이 남아있을 때 값을 비교하면서 삽입
		while (L <= mid && R <= right) {
			// 왼쪽 분할의 값이 작은 경우 왼쪽 분할의 값 삽입
			if (nums[L] <= nums[R]) {
				result[idx++] = nums[L++];
			} else {
				result[idx++] = nums[R++];
			}
		}

		// 왼쪽 구간에 값이 남아있는 경우
		if (L <= mid) {
			for (int i = L; i <= mid; i++) {
				result[idx++] = nums[i];
			}
		}

		// 오른쪽 구간에 값이 남아있는 경우
		else {
			for (int i = R; i <= right; i++) {
				result[idx++] = nums[i];
			}
		}

		// 정렬된 result의 값을 원래 배열에 저장
		for (int i = left; i <= right; i++) {
			nums[i] = result[i];
		}
	}
}
