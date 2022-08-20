import java.util.Scanner;
import java.util.Stack;

public class 괄호짝짓기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		//10개의 테스트케이스
		for (int t = 1; t <= 10; t++) {
			//문자열 길이
			int len = sc.nextInt();
			//문자열
			String str = sc.next();
			
			System.out.printf("#%d %d\n", t, check(str));
		}
	}
	
	//유효성 검사
	static int check(String str) {
		Stack<Character> stack = new Stack<>();

		// str을 배열로 만들기
		char[] arr = str.toCharArray();

		// 괄호가 올바르게 적혀있으면 1, 아니면 0
		int flag = 1;

		for (int i = 0; i < arr.length; i++) {
			// 여는 괄호는 모두 push
			if (arr[i] == '(' || arr[i] == '{' || arr[i] == '[') {
				stack.push(arr[i]);
			}
			// 닫는 괄호가 들어오면 pop하여 짝이 맞는지 확인
			else if (arr[i] == ')' || arr[i] == '}' || arr[i] == ']') {
				if ((arr[i] == ')') && (stack.pop() != '(')) {
					flag = 0;
					break;
				} else if ((arr[i] == '}') && (stack.pop() != '{')) {
					flag = 0;
					break;
				} else if ((arr[i] == ']') && (stack.pop() != '[')) {
					flag = 0;
					break;
				}
			}
			// 그 외 문자는 continue
			else {
				continue;
			}
		}

		// stack에 남아있으면 짝이 맞지 않으므로 flag = 0
		if (!stack.isEmpty()) {
			flag = 0;
		}

		return flag;
	}
}