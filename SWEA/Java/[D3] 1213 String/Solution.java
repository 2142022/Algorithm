import java.util.Scanner;

public class Solution {
	static char[] find;
	static char[] text;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		//10개의 테스트케이스
		for (int t = 0; t < 10; t++) {
			//테스트케이스 번호 입력받기
			int testcase = sc.nextInt();
			
			//찾을 문자열 입력받기
			String str = sc.next();
			find = str.toCharArray();
			
			//검색할 문장 입력받기
			str = sc.next();
			text = str.toCharArray();
			
			//검색하기
			int result = 0;
			
			for (int i = 0; i < text.length; i++) {
				//찾으려는 단어로 시작하고 찾으려는 문자열의 크기만큼 남아있을 때
				if ((text[i] == find[0]) && (i <= text.length - find.length)) {
					if (search(i)) {
						result++;
					}
				}
			}
			
			System.out.printf("#%d %d\n", testcase, result);
		}
	}
	
	static boolean search(int idx) {
		for (int i = 1; i < find.length; i++) {
			if (text[idx + i] != find[i]) {
				return false;
			}
		}
		return true;
	}
}