import java.util.Scanner;

public class 종이붙이기 {
	// result[i]: 가로의 길이가 10i인 직사각형을 만들 수 있는 경우의 수
	static int[] result;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 만들고자 하는 직사각형의 가로의 길이 / 10
			int N = sc.nextInt() / 10;

			// result[i]: 가로의 길이가 10 x i인 직사각형을 만들 수 있는 경우의 수
			result = new int[N + 1];

			// 가로의 길이가 N인 경우 = (가로의 길이가 N-1인 경우) + 2 X (가로의 길이가 N-2인 경우)
			// 예를 들어, N = 30일 때:
			// N = 20일 때의 경우에서 10짜리 종이를 붙일 수 있음 => result[N-1]
			// N = 10일 때의 경우에서 20짜리를 붙이는 경우와 10짜리 2개를 가로로 붙일 수 있음 => 2result[N-2]
			// f(n) = f(n-1) + 2f(n-2)
			result[1] = 1;
			result[2] = 3;
			f(N);

//			System.out.println(Arrays.toString(result));
			System.out.printf("#%d %d\n", t, result[N]);
		}
	}

	private static void f(int n) {
		for (int i = 3; i <= n; i++) {
			result[i] = result[i - 1] + 2 * result[i - 2];
		}
	}
}
