//import java.util.Arrays;
import java.util.Scanner;

public class 최대수_구하기 {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		// 테스트케이스 10개
		for (int t = 1; t < T + 1; t++) {

			// 10개의 숫자 입력받기
			int[] arr = new int[10];

			for (int i = 0; i < 10; i++) {
				arr[i] = sc.nextInt();
			}

			// 최댓값: 오름차순 정렬하여 맨 마지막 원소
//			Arrays.sort(arr);
			for (int i = 0; i < 9; i++) {
	            for (int j = 0; j < 9-i; j++) {
	                if (arr[j] > arr[j + 1]) {
	                    int tmp = arr[j];
	                    arr[j] = arr[j + 1];
	                    arr[j + 1] = tmp;
	                }
	            }
	        }

			System.out.printf("#%d %d\n", t, arr[9]);
		}
	}
}
