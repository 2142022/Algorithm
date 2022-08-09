import java.util.Scanner;

public class Flatten {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		
		//테스트케이스 10개
		for (int t=1; t<= 10; t++) {
			//덤프 제한 횟수 입력받기
			int dump = sc.nextInt();
			
			//상자의 높이 입력받기
			int[] height = new int[100];
			for (int i = 0; i < 100; i++) {
				height[i] = sc.nextInt();
			}
			
			//dump 횟수
			int cnt = 0;
			
			//cnt가 제한 횟수가 될 때까지 반복 수행
			// 한번은 무조건 정렬해야 하므로 do while문 사용
			do {
				//오름차순 정렬
				for (int i = 0; i < 99; i++) {
					for(int j = 0; j < 99-i; j++) {
						if (height[j] > height[j+1]) {
							int tmp = height[j];
							height[j] = height[j+1];
							height[j+1] = tmp;
						}
					}
				}
				
				//최대값과 최소값의 차이가 0이나 1이면 평탄화 완료
				if (height[99] - height[0] <= 1) {
					break;
				}
				
				//평탄화 작업 시작
				height[99]--;
				height[0]++;
				cnt++;
				
			} while (cnt < dump);
			
			//마지막 평탄화 작업으로 인해 최대값과 최소값이 변경될 수도 있음
			int result = Math.max(height[98], height[99]) - Math.min(height[0], height[1]);
			System.out.printf("#%d %d\n", t, result);
		}
	}
}
