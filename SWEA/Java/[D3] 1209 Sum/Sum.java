import java.util.Scanner;

public class Sum {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		//10개의 테스트케이스
		for (int k = 0; k < 10; k++) {
			
			//테스트케이스 번호 입력받기
			int testcase = sc.nextInt();
			
			//100X100 2차원 배열 입력받기
			int[][] map = new int[100][100];
			for (int i = 0; i < 100; i++) {
				for(int j = 0; j < 100; j++)
					map[i][j] = sc.nextInt();
			}
			
			int maxsum = 0;
			
			//한 행의 합을 구하고 max값과 비교
			for (int i = 0; i < 100; i++) {
				int sum = 0;
				
				for(int j = 0; j < 100; j++) {
					sum += map[i][j];
				}
				maxsum = Math.max(maxsum,  sum);
			}
			
			//한 열의 합을 구하고 max값과 비교
			for (int j = 0; j < 100; j++) {
				int sum = 0;
				
				for(int i = 0; i < 100; i++) {
					sum += map[i][j];
				}
				maxsum = Math.max(maxsum,  sum);
			}
			
			//좌측 상단에서 우측 하단으로 가는 대각선의 합 구하기
		    int sum = 0;
		    for (int i = 0; i < 100; i++) {
		        for (int j = 0; j < 100; j++) {
		            if (i == j) {
		                sum += map[i][j];
		            }
		        }
		    }
		    maxsum = Math.max(maxsum, sum);
			
		    //우측 상단에서 좌측 하단으로 가는 대각선의 합 구하기
		    sum = 0;
		    for (int i = 0; i < 100; i++) {
		        for (int j = 0; j < 100; j++) {
		            if (i + j == 198) {
		                sum += map[i][j];
		            }
		        }
		    }
		    maxsum = Math.max(maxsum, sum);
		    
		    System.out.printf("#%d %d\n", testcase, maxsum);
		}
	}
}
