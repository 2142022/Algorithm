import java.util.Scanner;

public class 딱지놀이 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 총 라운드 수
		int N = sc.nextInt();

		// N번의 라운드
		for (int n = 0; n < N; n++) {
			// A가 가진 총 딱지 그림 개수
			int numA = sc.nextInt();

			// A가 가진 딱지 그림 각각의 개수
			int[] A = new int[5];
			for (int i = 0; i < numA; i++) {
				A[sc.nextInt()]++;
			}

			// B가 가진 총 딱지 그림 개수
			int numB = sc.nextInt();

			// B가 가진 딱지 그림 각각의 개수
			int[] B = new int[5];
			for (int i = 0; i < numB; i++) {
				B[sc.nextInt()]++;
			}

			// 승자 확인
			char win = 'D';
			for (int i = 4; i > 0; i--) {
				if (A[i] > B[i]) {
					win = 'A';
					break;
				} else if (A[i] < B[i]) {
					win = 'B';
					break;
				}
			}

			System.out.println(win);
		}
	}
}
