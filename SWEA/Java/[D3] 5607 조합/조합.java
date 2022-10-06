import java.util.Scanner;

public class 조합 {
	static int div = 1234567891;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// N combination R
			int N = sc.nextInt();
			int R = sc.nextInt();

			// i! % 1234567891을 담은 배열
			// N은 1000000 이하이므로 배열의 크기는 1000001
			long[] factorial = new long[1000001];
			factorial[0] = 1;
			for (int i = 1; i < 1000001; i++) {
				factorial[i] = (i * factorial[i - 1]) % div;
			}

			// N combination R = N! / ((N-R)!R!)
			// 페르마의 정리 이용
			// 1234567891은 소수이므로 (N-R)!R!과 서로소
			// (정확히는 factorial[N-R] * factorial[R]과 서로소)
			// 따라서, ((N-R)!R!)^(-1) = ((N-R)!R!)^(1234567891 - 2) (mod 1234567891)
			long result = (factorial[N - R] * factorial[R]) % div;
			result = power(result, div - 2);
			result = (factorial[N] * result) % div;
			System.out.printf("#%d %d\n", t, result);
		}
	}

	private static long power(long n, int p) {
		if (p == 1) {
			return n;
		}

		long tmp = power(n, p / 2);

		// 홀수 승인 경우
		if (p % 2 == 1) {
			return (((tmp * tmp) % div) * n) % div;
		}

		// 짝수 승인 경우
		else {
			return (tmp * tmp) % div;
		}
	}
}
