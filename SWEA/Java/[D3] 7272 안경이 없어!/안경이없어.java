import java.util.Scanner;

public class 안경이없어 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 문자열
			char[] str1 = sc.next().toCharArray();
			char[] str2 = sc.next().toCharArray();

			// 문자 비교 (같으면 1, 다르면 0)
			int flag = 1;

			// 문자열의 길이가 다르면 안됨
			if (str1.length != str2.length) {
				flag = 0;
			} else {
				// 문자 하나씩 비교
				for (int i = 0; i < str1.length; i++) {
					if (op(str1[i]) != op(str2[i])) {
						flag = 0;
						break;
					}
				}
			}

			if (flag == 1) {
				System.out.printf("#%d SAME\n", t);
			} else {
				System.out.printf("#%d DIFF\n", t);
			}
		}
	}

	// 구멍의 개수
	static int op(char c) {
		if (c == 'B') {
			return 2;
		} else if (c == 'A' || c == 'D' || c == 'O' || c == 'P' || c == 'Q' || c == 'R') {
			return 1;
		} else {
			return 0;
		}
	}
}
