import java.util.Scanner;

public class 숫자를_정렬하자 {
	// 합수에서 배열을 사용하기 위해 static으로 배열 선언
	static int[] arr;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트 케이스 입력받고 실행
		int T = sc.nextInt();

		for (int t = 1; t <= T; t++) {

			// 숫자 개수 및 숫자 배열로 입력받기
			int N = sc.nextInt();
			arr = new int[N];

			for (int i = 0; i < N; i++) {
				arr[i] = sc.nextInt();
			}

//			// 정렬 방법1: 버블 정렬
//			bubbleSort(arr, N);

			// 정렬 방법2: 선택 정렬
			selectionSort(arr, N);

			// 출력하기
			System.out.printf("#%d", t);
			for (int i = 0; i < N; i++) {
				System.out.printf(" %d", arr[i]);
			}
			System.out.println();
		}
	}

	static void bubbleSort(int[] arr, int N) {
		for (int i = 0; i < N - 1; i++) {
			for (int j = 0; j < N - i - 1; j++) {
				if (arr[j] > arr[j + 1]) {
					swap(j, j + 1);
				}
			}
		}
	}

	static void selectionSort(int[] arr, int N) {
		for (int i = 0; i < N - 1; i++) {
			int minIdx = i;

			for (int j = i + 1; j < N; j++) {
				if (arr[j] < arr[minIdx]) {
					swap(j, minIdx);
				}
			}
		}
	}

	static void swap(int a, int b) {
		int tmp = arr[a];
		arr[a] = arr[b];
		arr[b] = tmp;
	}
}
