import java.util.Scanner;

public class N과M3 {

	static int N;
	static int M;

	static int[] nums;
	static int[] result;

	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// N개의 자연수(1~N) 중 M개를 뽑는 모든 경우의 수 구하기
		N = sc.nextInt();
		M = sc.nextInt();

		// 1 ~ N
		nums = new int[N];
		for (int i = 0; i < N; i++) {
			nums[i] = i + 1;
		}

		// 결과
		result = new int[M];

		// 순열
		permutation(0);

		System.out.println(sb);
	}

	static void permutation(int cnt) {
		// 결과에 M개의 원소가 들어가면 끝내기
		if (cnt == M) {
			for (int i = 0; i < M; i++) {
				sb.append(result[i]).append(" ");
			}
			sb.append("\n");
			return;
		}

		// N개의 원소를 돌면서 permutation 재귀
		for (int i = 0; i < N; i++) {
			// 결과에 포함시키기
			result[cnt] = nums[i];

			// 개수를 하나 증가시키고 재귀
			permutation(cnt + 1);
		}
	}
}
