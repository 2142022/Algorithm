import java.util.Scanner;

public class 중간_평균값_구하기 {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		// 테스트 케이스 입력받고 실행
		int T = sc.nextInt();

		for (int t = 1; t <= T; t++) {

			// 10개의 숫자 배열로 입력받기
			int[] arr = new int[10];

			for (int i = 0; i < 10; i++) {
				arr[i] = sc.nextInt();
			}

			// 오름차순 정렬하기
			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 9 - i; j++) {
					if (arr[j] > arr[j + 1]) {
						int tmp = arr[j];
						arr[j] = arr[j + 1];
						arr[j + 1] = tmp;
					}
				}
			}

			// 최대, 최소 원소 제외 평균값 구하기
			int result = 0;
			for (int i = 1; i < 9; i++) {
				result += arr[i];
			}
			result = (result + 4) / 8; // 반올림을 위해 +4

			System.out.printf("#%d %d\n", t, result);
		}
	}
}
