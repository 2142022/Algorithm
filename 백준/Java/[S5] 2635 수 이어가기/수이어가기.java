import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class 수이어가기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 처음 수 입력받기
		List<Integer> result = new ArrayList<>();
		result.add(sc.nextInt());

		// 각각의 경우
		for (int i = 0; i <= result.get(0) / 2; i++) {
			List<Integer> tmp = new ArrayList<>();
			tmp.add(result.get(0));
			tmp.add(result.get(0) - i);

			// 두 수의 차가 음수가 될 때까지 추가
			while (tmp.get(tmp.size() - 2) - tmp.get(tmp.size() - 1) >= 0) {
				tmp.add(tmp.get(tmp.size() - 2) - tmp.get(tmp.size() - 1));
			}

			// tmp 원소가 더 많으면 result로 바꾸기
			if (tmp.size() > result.size()) {
				result = tmp;
			}
		}

		// 최대 개수 출력
		System.out.println(result.size());

		// 수 출력
		for (int i = 0; i < result.size(); i++) {
			System.out.print(result.get(i) + " ");
		}
	}
}
