
//import java.util.Arrays;
import java.util.Scanner;

public class 중간값_찾기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 입력받을 숫자의 개수 입력받기
		int N = sc.nextInt();

		// N개의 숫자 배열로 입력 받기
		int[] arr = new int[N];

		for (int i = 0; i < N; i++) {
			arr[i] = sc.nextInt();
		}

		// 중간값: 오름차순 정렬 후 중간에 있는 값
//		Arrays.sort(arr);
		for (int i = 0; i < N - 1; i++) {
			for (int j = 0; j < N - i - 1; j++) {
				if (arr[j] > arr[j + 1]) {
					int tmp = arr[j];
					arr[j] = arr[j + 1];
					arr[j + 1] = tmp;
				}
			}
		}

		System.out.println(arr[N / 2]);
	}
}
