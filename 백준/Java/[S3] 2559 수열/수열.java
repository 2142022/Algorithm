import java.util.Scanner;

public class 수열 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 온도의 개수
		int N = sc.nextInt();

		// 연속적인 날짜
		int K = sc.nextInt();

		// N개의 온도
		int[] temp = new int[N];
		for (int i = 0; i < N; i++) {
			temp[i] = sc.nextInt();
		}

		// 온도 합의 최대값
		int max = -2147483648;

		// 온도 합
		for (int i = 0; i < N - K + 1; i++) {
			int sum = 0;

			for (int j = i; j < i + K; j++) {
				sum += temp[j];
			}

			max = Math.max(max, sum);
		}

		System.out.println(max);
	}
}
