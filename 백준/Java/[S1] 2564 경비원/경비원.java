import java.util.Scanner;

public class 경비원 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 블록의 가로, 세로 길이
		int width = sc.nextInt();
		int height = sc.nextInt();

		// 블록이 아닌 직선상으로 생각하기 (북 -> 동 -> 남 -> 서)
		// 전체 길이
		int len = 2 * (width + height);

		// 상점의 개수
		int N = sc.nextInt();

		// 상점의 위치
		int[] store = new int[N];
		for (int i = 0; i < N; i++) {
			// 동, 서, 남, 북에 따라 직선 상에서의 위치 구하기
			switch (sc.nextInt()) {
			// 북
			case 1:
				store[i] = sc.nextInt();
				break;
			// 남
			case 2:
				store[i] = width + height + width - sc.nextInt();
				break;
			// 서
			case 3:
				store[i] = len - sc.nextInt();
				break;
			// 동
			case 4:
				store[i] = width + sc.nextInt();
				break;
			}
		}

		// 동근이의 위치
		int loc = 0;
		// 동, 서, 남, 북에 따라 직선 상에서의 위치 구하기
		switch (sc.nextInt()) {
		// 북
		case 1:
			loc = sc.nextInt();
			break;
		// 남
		case 2:
			loc = width + height + width - sc.nextInt();
			break;
		// 서
		case 3:
			loc = len - sc.nextInt();
			break;
		// 동
		case 4:
			loc = width + sc.nextInt();
			break;
		}

		// 최단 거리의 합
		int min = 0;

		// 상점까지의 거리
		for (int i = 0; i < N; i++) {
			int tmp = Math.abs(loc - store[i]);
			min += Math.min(tmp, len - tmp);
		}

		System.out.println(min);
	}
}
