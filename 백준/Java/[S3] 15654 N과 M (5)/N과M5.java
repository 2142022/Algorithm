import java.util.Scanner;

public class N과M5 {

	static int N;
	static int M;

	static int[] nums;
	static int[] result;
	static int[] flag;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// N개의 자연수(1~N) 중 M개를 뽑는 모든 경우의 수 구하기
		N = sc.nextInt();
		M = sc.nextInt();

		// 1 ~ N
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

		// 결과
		result = new int[M];

		// 결과에 포함하면 1, 아니면 0
		flag = new int[N];

		// 순열
		permutation(0);
	}

	static void permutation(int cnt) {
		// 결과에 M개의 원소가 들어가면 끝내기
		if (cnt == M) {
			for (int i = 0; i < M; i++) {
				System.out.print(result[i] + " ");
			}
			System.out.println();
			return;
		}

		// N개의 원소를 돌면서 permutation 재귀
		for (int i = 0; i < N; i++) {
			// 아직 결과에 포함되지 않았다면
			if (flag[i] == 0) {
				// 결과에 포함시키기
				flag[i] = 1;
				result[cnt] = nums[i];

				// 개수를 하나 증가시키고 재귀
				permutation(cnt + 1);

				// 다시 결과에서 제외
				flag[i] = 0;
			}
		}
	}
}
