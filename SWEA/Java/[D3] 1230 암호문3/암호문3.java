import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class 암호문3 {
	static Scanner sc = new Scanner(System.in);

	// 원본 암호문
	static List<Integer> encryption = new ArrayList<>();

	public static void main(String[] args) {
		// 10개의 테스트케이스
		for (int t = 1; t <= 10; t++) {
			// 원본 암호문의 길이
			int N = sc.nextInt();

			// 원본 암호문 초기화 후 입력받기
			encryption.clear();
			for (int i = 0; i < N; i++) {
				encryption.add(sc.nextInt());
			}

			// 명령어 개수
			int M = sc.nextInt();

			// M번의 명령어 실행
			for (int i = 0; i < M; i++) {
				char order = sc.next().charAt(0);

				if (order == 'I') {
					insert();
				} else if (order == 'D') {
					delete();
				} else if (order == 'A') {
					add();
				}
			}

			// 출력
			System.out.print("#" + t);
			for (int i = 0; i < 10; i++) {
				System.out.print(" " + encryption.get(i));
			}
			System.out.println();
		}
	}

	static void insert() {
		// 삽입 위치
		int x = sc.nextInt();

		// 삽입 숫자 개수
		int y = sc.nextInt();

		// 숫자 삽입
		for (int i = 0; i < y; i++) {
			encryption.add(x + i, sc.nextInt());
		}
	}

	static void delete() {
		// 삭제 위치
		int x = sc.nextInt();

		// 삭제 숫자 개수
		int y = sc.nextInt();

		// 숫자 삭제
		for (int i = 0; i < y; i++) {
			encryption.remove(x);
		}
	}

	static void add() {
		// 추가 숫자 개수
		int y = sc.nextInt();

		// 숫자 추가
		for (int i = 0; i < y; i++) {
			encryption.add(sc.nextInt());
		}
	}
}
