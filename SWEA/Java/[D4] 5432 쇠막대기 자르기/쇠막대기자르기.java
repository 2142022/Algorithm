import java.util.Scanner;
import java.util.Stack;

public class 쇠막대기자르기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 괄호 입력받기
			char[] origin = sc.next().toCharArray();

			// 결과 출력
			System.out.printf("#%d %d\n", t, solve(origin));
		}
	}

	// 쇠막대기 개수 세기
	static int solve(char[] origin) {
		//쇠막대기 개수 
		int result = 0;
		
		//'('를 저장하는 스택
		Stack<Character> stack = new Stack<>();
		
		for (int i = 0; i < origin.length; i++) {
			//레이저인 경우 스택에 있는 '(' 개수만큼 result에 더하기
			if (origin[i] == '(' && origin[i+1] == ')') {
				i++;
				result += stack.size();
			}
			
			//막대기가 시작되면 스택에 저장
			else if (origin[i] == '(') {
				stack.push(origin[i]);
			}
			
			//막대기가 끝나면 스택에서 제거하고 쇠막대기 개수 1 증가
			else if (origin[i] == ')') {
				stack.pop();
				result++;
			}
		}
		
		return result;
	}
}