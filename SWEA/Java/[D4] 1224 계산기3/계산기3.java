import java.util.Scanner;
import java.util.Stack;

public class 계산기3 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 10개의 테스트케이스
		for (int t = 1; t <= 10; t++) {
			// 문자열 계산식 길이
			int len = sc.nextInt();
			// 문자열 계산식 입력받고 바로 char[]로 변환
			char[] origin = sc.next().toCharArray();

			System.out.printf("#%d %d\n", t, cal(transform(origin)));
		}
	}

	static char[] transform(char[] origin) {
		// 1. 후위 표기식으로 변경한다. (스택 : 연산자) : Stack<Character>
		Stack<Character> opStack = new Stack<>();
		int N = 0;
		for (int i = 0; i < origin.length; i++) {
			if (origin[i] != '(' && origin[i] != ')') {
				N++;
			}
		}
		char[] result = new char[N];
		int idx = 0;

		// 1-1. 토큰을 읽는다. (요소를 하나씩 읽는다.)
		for (int i = 0; i < origin.length; i++) {
			// 1-2. 피연산자라면 출력한다.
			if (origin[i] >= '0' && origin[i] <= '9') {
				result[idx++] = origin[i];
			}

			// 1-3. 연산자라면....
			else if (origin[i] == '(' || origin[i] == '+' || origin[i] == '-' || origin[i] == '*' || origin[i] == '/') {
				// 1-3-1. 스택이 공백상태라면 그냥 넣는다.
				if (opStack.isEmpty()) {
					opStack.push(origin[i]);
				}

				// 1-3-2. 스택이 공백상태가 아니라면 top이 현재가 가리키고 있는 연산자와 읽은 연산자를 비교하여 내가 찍어누를 수 있을 떄만 넣는다.
				// 1-3-3. 연산자의 우선순위는 ( 안 : 0, 밖 : 3 | * / 안밖 : 2 | + - 안밖 : 1 )얘는 어차피 넣지 않을 친구라
				else {
					if (opOrder(origin[i]) > opOrder(opStack.peek()) || origin[i] == '(') {
						opStack.push(origin[i]);
					} else {
						while ((!opStack.isEmpty()) && (opOrder(origin[i]) <= opOrder(opStack.peek()))) {
							result[idx++] = opStack.pop();
						}
						opStack.push(origin[i]);
					}
				}
			}

			// 1-4. 닫는 소괄호 라면 여는 소괄호를 만날때까지 pop하여 출력하고, ( 얘는 출력하지 않고 pop한다.
			else if (origin[i] == ')') {
				while ((opStack.peek() != '(') && (idx < N)) {
					result[idx++] = opStack.pop();
				}
				opStack.pop(); // '(' pop
			}
		} // 1-5. 토큰을 전부 읽을 때까지 반복한다.

		// 1-6. 토큰을 다 읽었는데 스택이 공백이 아니라면 스택이 공백상태가 될때까지 pop하여 출력한다.
		while ((!opStack.isEmpty()) && (idx < N)) {
			if (opStack.peek() == '(')
				opStack.pop();
			result[idx++] = opStack.pop();
		}

		return result;
	}

	static int opOrder(char c) {
		switch (c) {
		case '(':
			return 0;
		case '+':
		case '-':
			return 1;
		case '*':
		case '/':
			return 2;
		default:
			return -1;
		}
	}

	static int cal(char[] arr) {
		// 2. 변경한 후위표기식을 계산한다. (스택 : 피연산자) : Stack<Integer>
		Stack<Integer> numStack = new Stack<>();

		// 2-1. 토큰을 읽는다. (요소를 하나씩 읽는다.)
		for (int i = 0; i < arr.length; i++) {
			// 2-2. 피연산자라면 스택에 넣는다.
			if (arr[i] >= '0' && arr[i] <= '9') {
				numStack.push(arr[i] - '0'); // int로 변환 후 push
			}

			// 2-3. 연산자라면 필요한 피연산자만큼 꺼내어 계산하고 다시 결과를 집어 넣는다. (순서가 중요하다.!!!!!)
			else {
				int b = numStack.pop();
				int a = numStack.pop();

				switch (arr[i]) {
				case '+':
					numStack.push(a + b);
					break;
				case '-':
					numStack.push(a - b);
					break;
				case '*':
					numStack.push(a * b);
					break;
				case '/':
					numStack.push(a / b);
					break;
				}
			}
		} // 2-4. 토큰을 전부 읽을 때까지 반복한다.

		// 2-5. 토큰을 다 읽고 처리했다면, 마지막으로 pop 하여 결과를 출력한다.
		return numStack.pop();
	}
}