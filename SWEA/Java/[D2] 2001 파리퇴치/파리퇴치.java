import java.util.Scanner;

public class 파리퇴치 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		//테스트케이스 입력받고 실행
		int T = sc.nextInt();
		for (int t = 1; t <= T; t++) {
			//N, M, 배열값 입력받기
			int N = sc.nextInt();
			int M = sc.nextInt();
			int[][] arr = new int[N][N];
			
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			
			//최댓값 비교하기
			int max = 0;
			for (int i = 0; i < N-M+1; i++) {
				for (int j = 0; j < N-M+1; j++) {
					int result = 0;
					for (int m = 0; m < M; m++) {
						for(int n = 0; n < M; n++)
						result += arr[i+m][j+n];
					}
					
					max = Math.max(max, result);
				}
			}
			
			System.out.printf("#%d %d\n", t, max);
		}
	}
}
