import java.util.Scanner;

public class 직사각형을만드는방법 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 정사각형의 개수
		int n = sc.nextInt();

		System.out.println(count(n, 0));
	}

	// n개의 정사각형으로 만들 수 있는 직사각형의 개수: n의 약수의 개수 / 2
	static int count(int n, int result) {
		if (n == 1) {
			return result + 1;
		}

		int cnt = 0;

		// n의 약수의 개수
		for (int i = 1; i <= n; i++) {
			if (n % i == 0) {
				cnt++;
			}
		}

		// n의 약수의 개수가 짝수일 때와 홀수일 때
		if (cnt % 2 == 0) {
			result = result + cnt / 2;
		} else {
			result = result + cnt / 2 + 1;
		}

		// 재귀함수 n이 1일 때까지 구하기
		return count(n - 1, result);
	}
}
