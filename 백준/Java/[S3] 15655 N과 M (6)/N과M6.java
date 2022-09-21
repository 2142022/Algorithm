import java.util.Scanner;

public class N과M6 {

	// N개의 자연수(1~N) 중에서 M개의 자연수 뽑기
	static int N;
	static int M;

	// N개의 자연수
	static int[] nums;

	// 뽑은 M개의 자연수
	static int[] result;

	static StringBuilder sb;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		sb = new StringBuilder();

		// N개의 자연수 중에서 M개의 자연수 뽑기
		N = sc.nextInt();
		M = sc.nextInt();

		// N개의 자연수 입력받기
		nums = new int[N];
		for (int i = 0; i < N; i++) {
			nums[i] = sc.nextInt();
		}

		// nums 오름차순 정렬
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N - 1; j++) {
				if (nums[j] > nums[j + 1]) {
					int tmp = nums[j];
					nums[j] = nums[j + 1];
					nums[j + 1] = tmp;
				}
			}
		}

		// 뽑은 M개의 자연수
		result = new int[M];

		// 조합을 이용하여 M개의 자연수 뽑기
		combination(0, 0);

		System.out.println(sb);
	}

	private static void combination(int idx, int cnt) {
		// M개의 수를 뽑으면 그만두기
		if (cnt == M) {
			for (int i = 0; i < M; i++) {
				sb.append(result[i]).append(" ");
			}
			sb.append("\n");
			return;
		}

		for (int i = idx; i < N; i++) {
			// 결과에 값 넣기
			result[cnt] = nums[i];

			// 재귀로 다음 값 구하기
			combination(i + 1, cnt + 1);
		}
	}
}