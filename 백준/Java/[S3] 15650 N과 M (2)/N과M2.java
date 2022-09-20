import java.util.Scanner;

public class N과M2 {

	// N개의 자연수(1~N) 중에서 M개의 자연수 뽑기
	static int N;
	static int M;

	// N개의 자연수
	static int[] nums;

	// 뽑은 M개의 자연수
	static int[] result;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// N개의 자연수(1~N) 중에서 M개의 자연수 뽑기
		N = sc.nextInt();
		M = sc.nextInt();

		// N개의 자연수
		nums = new int[N];
		for (int i = 0; i < N; i++) {
			nums[i] = i + 1;
		}

		// 뽑은 M개의 자연수
		result = new int[M];

		// 조합을 이용하여 M개의 자연수 뽑기
		combination(0, 0);
	}

	private static void combination(int idx, int cnt) {
		// M개의 수를 뽑으면 그만두기
		if (cnt == M) {
			for (int i = 0; i < M; i++) {
				System.out.print(result[i] + " ");
			}
			System.out.println();
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
