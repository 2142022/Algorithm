import java.util.Arrays;
import java.util.Scanner;

public class 문제제목붙이기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 문제의 개수
			int N = sc.nextInt();

			// 문제 제목의 맨 앞 글자만 입력받기
			int[] title = new int[N];
			for (int i = 0; i < N; i++) {
				title[i] = sc.next().charAt(0);
			}

			// 오름차순으로 정렬
			Arrays.sort(title);

			// 이전 알파벳과 같다면 넘어가고, 다음 알파벳이면 개수 증가, 그 외에는 break
			int alpha = 'A';
			int cnt = 0;
			if (title[0] == alpha++) {
				cnt++;
				for (int i = 1; i < N; i++) {
					if (title[i] == title[i - 1]) {
						continue;
					} else if (title[i] == alpha++) {
						cnt++;
					} else {
						break;
					}
				}
			}

			// 출력
			System.out.printf("#%d %d\n", t, cnt);
		}
	}
}
