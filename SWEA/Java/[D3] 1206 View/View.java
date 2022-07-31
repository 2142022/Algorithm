import java.util.Arrays;
import java.util.Scanner;

public class View {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		// 10번 반복
		for (int j = 0; j < 10; j++) {

			// 테스트케이스 길이
			int length = sc.nextInt();
			// 각 테스트케이스의 결과
			int result = 0;
			
			//공백을 기준으로 map 입력받기
			int[] arr = new int[length];
			for(int i = 0; i < length; i++) {
				arr[i] = sc.nextInt();
			}
			
			//앞뒤 2칸씩 0이므로 2부터 length-2까지
			for (int i = 2; i < length - 2; i++) {
				
				//5개 원소로 새로운 배열 만들기
				int[] tmp = {arr[i-2], arr[i-1], arr[i], arr[i+1], arr[i+2]};
				
				//오름차순 정렬
				Arrays.sort(tmp);
				
				//자기 자신이 최대값이면 조망권 확보
				if (tmp[4] == arr[i]) {
					
					//조망권 확보 세대 수는 (tmp[4] - tmp[3])
					result = result + tmp[4] - tmp[3];
				}
				
			}
			System.out.printf("\n#%d %d", j+1, result);
		}
	}
}