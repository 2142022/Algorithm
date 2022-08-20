import java.util.Scanner;

public class 원재의메모리복구하기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		//테스트케이스 개수
		int T = sc.nextInt();
		
		//T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			//현재 메모리 상태를 배열로 입력받기
			char[] memory = sc.next().toCharArray();
			
			//0에서 1로 바뀌거나 1에서 0으로 바뀌는 경우 cnt++
			int cnt = 0;
			for (int i = 1; i < memory.length; i++) {
				if (memory[i] - '0' + memory[i-1] - '0' == 1) {
					cnt++;
				}
			}
			
			//첫 원소가 1인 경우에는 +1
			if (memory[0] - '0' == 1) {
				cnt++;
			}
			
			//출력
			System.out.printf("#%d %d\n", t, cnt);
		}
	}
}
