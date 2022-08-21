import java.util.Scanner;

public class 스위치켜고끄기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 스위치 개수
		int N = sc.nextInt();

		// 스위치 상태
		int[] flag = new int[N];
		for (int i = 0; i < N; i++) {
			flag[i] = sc.nextInt();
		}

		// 학생 수
		int P = sc.nextInt();

		// 학생의 성별 및 학생이 받은 수
		int[][] student = new int[P][2];
		for (int i = 0; i < P; i++) {
			student[i][0] = sc.nextInt();
			student[i][1] = sc.nextInt();
		}

		// 스위치 상태 바꾸기
		for (int i = 0; i < P; i++) {
			// 남학생인 경우
			if (student[i][0] == 1) {
				for (int j = 0; j < N; j++) {
					if ((j + 1) % student[i][1] == 0) {
						flag[j] = 1 - flag[j];
					}
				}
			}

			// 여학생의 경우
			else if (student[i][0] == 2) {
				// 받은 번호를 스위치의 인덱스로 하기 위해 -1
				int num = student[i][1] - 1;

				// 받은 번호의 스위치 바꾸기
				flag[num] = 1 - flag[num];

				// 양 옆으로 비교하면서 바꾸기
				int j = 1;
				while ((num - j >= 0) && (num + j < N)) {
					// 양 옆 스위치의 상태가 같다면 바꾸기
					if (flag[num - j] == flag[num + j]) {
						flag[num - j] = 1 - flag[num - j];
						flag[num + j] = 1 - flag[num + j];
					}

					// 스위치의 상태가 다르다면 그만두기
					else {
						break;
					}

					j++;
				}
			}
		}

		// 스위치 출력
		for (int i = 0; i < N; i++) {
			System.out.print(flag[i] + " ");
			if ((i + 1) % 20 == 0) {
				System.out.println();
			}
		}
	}
}
