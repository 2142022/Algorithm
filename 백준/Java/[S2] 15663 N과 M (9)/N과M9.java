import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.Scanner;

public class N과M9 {

	static int N;
	static int M;

	static int[] nums;
	static int[] result;
	static int[] flag;

	// 동일한 결과값 체크하기 위해 LinkedHashSet 사용
	// HashSet은 원소의 순서가 바뀌기 때문에 사용 불가
	static LinkedHashSet<String> ans;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// N개의 자연수 중 M개를 뽑는 모든 경우의 수 구하기
		N = sc.nextInt();
		M = sc.nextInt();

		// 숫자 입력받기
		nums = new int[N];
		for (int i = 0; i < N; i++) {
			nums[i] = sc.nextInt();
		}

		// nums 오름차순 정렬
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N - 1; j++) {
				if (nums[j] > nums[j + 1]) {
					int tmp = nums[j];
					nums[j] = nums[j + 1];
					nums[j + 1] = tmp;
				}
			}
		}

		// 결과
		result = new int[M];

		// 결과에 포함하면 1, 아니면 0
		flag = new int[N];

		// 동일한 결과값 체크하기 위해 LinkedHashSet 사용
		// HashSet은 원소의 순서가 바뀌기 때문에 사용 불가
		ans = new LinkedHashSet<>();

		// 순열
		permutation(0);

		Iterator<String> it = ans.iterator();
		while (it.hasNext()) {
			System.out.println(it.next());
		}
	}

	static void permutation(int cnt) {
		// 결과에 M개의 원소가 들어가면 끝내기
		if (cnt == M) {
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < M; i++) {
				sb.append(result[i]).append(" ");
			}

			// LinkedHashSet에 추가
			ans.add(sb.toString());
			return;
		}

		// N개의 원소를 돌면서 permutation 재귀
		for (int i = 0; i < N; i++) {
			// 아직 결과에 포함되지 않았다면
			if (flag[i] == 0) {
				// 결과에 포함시키기
				flag[i] = 1;
				result[cnt] = nums[i];

				// 개수를 하나 증가시키고 재귀
				permutation(cnt + 1);

				// 다시 결과에서 제외
				flag[i] = 0;
			}
		}
	}
}