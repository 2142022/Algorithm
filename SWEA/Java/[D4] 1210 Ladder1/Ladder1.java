import java.util.Scanner;

public class Ladder1 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		//10개의 테스트케이스
		for (int t = 0; t < 10; t++) {
			int testcase = sc.nextInt();
			
			//도착지점
			int r = 99;
			int c = -1;
			
			//map 입력받기
			int[][] map = new int[100][100];
			for (int i = 0; i < 100; i++) {
				for (int j = 0; j < 100; j++) {
					map[i][j] = sc.nextInt();
					if (map[i][j] == 2) {
						c = j;
					}
				}
			}

			//무한 반복
			while (true) {
				//위로 한 칸 이동
				r--;
				
				// 0행이 되면 중지
				if (r == 0) {
					System.out.printf("#%d %d\n", testcase, c);
					break;
				} 
				// 왼쪽에 1이 있는 경우 0이 나올 때까지 좌로 이동
				else if (c > 0 && map[r][c - 1] == 1) {
					do {
						c--;
					} while (c > 0 && map[r][c-1] == 1);
					
				} 
				//오른쪽에 1이 있는 경우 0이 나올 때까지 우로 이동
				else if (c < 99 && map[r][c+1] == 1) {
					do {
						c++;
					} while (c < 99 && map[r][c+1] == 1);
				}
			}
		}
	}
}
