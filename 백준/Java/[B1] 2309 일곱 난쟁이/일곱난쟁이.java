import java.util.Scanner;

public class 일곱난쟁이 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 아홉 명의 키 입력받기
		int[] h = new int[9];

		// 아홉 명 키의 합
		int sum = 0;

		for (int i = 0; i < 9; i++) {
			h[i] = sc.nextInt();
			sum += h[i];
		}

		// 오름차순 정렬 (삽입 정렬)
		for (int i = 1; i < 9; i++) {
			int tmp = h[i];
			int j;
			for (j = i - 1; j >= 0 && h[j] > tmp; j--) {
				h[j + 1] = h[j];
			}

			h[++j] = tmp;
		}

		// 난쟁이가 아닌 두 명의 인덱스
		int[] idx = find(h, sum);

		// 난쟁이가 아닌 사람만 출력
		for (int i = 0; i < 9; i++) {
			if (h[i] == h[idx[0]] || h[i] == h[idx[1]]) {
				continue;
			} else {
				System.out.println(h[i]);
			}
		}

	}

	// 난쟁이가 아닌 두 명 찾기
	static int[] find(int[] h, int sum) {

		// 두 명의 합이 sum - 100일 때 두 명의 인덱스 구하기
		int[] idx = new int[2];
		sum -= 100;
		for (int i = 0; i < 8; i++) {
			for (int j = i + 1; j < 9; j++) {
				if (h[i] + h[j] == sum) {
					idx[0] = i;
					idx[1] = j;
					return idx;
				}
			}
		}

		return null;
	}
}
