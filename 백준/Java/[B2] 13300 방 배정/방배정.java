import java.util.Scanner;

public class 방배정 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 학생 수
		int N = sc.nextInt();

		// 한 방 최대 인원 수
		int K = sc.nextInt();

		// 학생의 성별과 학년 입력받기
		int[][] student = new int[2][7];
		for (int i = 0; i < N; i++) {
			student[sc.nextInt()][sc.nextInt()]++;
		}

		// 필요한 방의 수
		int cnt = 0;
		for (int i = 0; i < 2; i++) {
			for (int j = 1; j < 7; j++) {
				if (student[i][j] == 0) {
					continue;
				} else {
					if (student[i][j] % K == 0) {
						cnt = cnt + student[i][j] / K;
					} else {
						cnt = cnt + student[i][j] / K + 1;
					}
				}
			}
		}

		// 출력
		System.out.println(cnt);
	}
}
