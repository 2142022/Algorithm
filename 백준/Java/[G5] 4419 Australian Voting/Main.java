import java.util.*;
import java.util.Map.Entry;

public class Main {
	
	// 투표 내역 수
	static int v = 0;
	// 각 투표 내역
	static List<List<Integer>> votes = new ArrayList<>();
	// 현재 투표 결과
	static HashMap<Integer, Integer> results;
	// 후보자 수
	static int n;
	// 각 후보자의 이름
	static String[] candidates;
	// 남아있는 후보자의 번호
	static HashSet<Integer> remains = new HashSet<>();
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		// 후보자 수
		n = sc.nextInt(); sc.nextLine();
		// 각 후보자의 이름
		candidates = new String[n + 1];
		
		// 모든 후보의 이름 저장하기
		for(int i = 1; i <= n; i++) {
			candidates[i] = sc.nextLine();
			remains.add(i);
		}
		
		// 모든 투표 내역 저장하기
		while (sc.hasNextInt()) {
			// 한 유권자의 투표 내역만 저장하기
			List<Integer> vote = new ArrayList<>();
			for (int i = 0; i < n; i++) {
				vote.add(sc.nextInt());
			}
			
			// 현재 투표 내역 추가하기
			votes.add(vote);
			// 투표 내역 수 증가시키기
			v++;
		}
		sc.close();
		
		// 당선될 때까지 투표 반복하기
		do {
			// 투표 내역을 이용하여 각 후보의 득표 수 구하기
			results = new HashMap<>();
			for (int i : remains) {
				results.put(i, 0);
			}
			for (int i = 0; i < v; i++) {
				// 득표 수 1개 증가
				int idx = votes.get(i).get(0);
				int now = results.get(idx);
				results.put(idx, ++now);
			}
		} while(!isFinish());
		
	}

	// 현재 투표 결과로 당선된 후보자가 있는지 확인
	private static boolean isFinish() {
		Set<Entry<Integer, Integer>> entrySet = results.entrySet();
		// 가장 많은 득표 수
		int max = Collections.max(results.values());
		// 가장 적은 득표 수
		int min = Collections.min(results.values());
		
		// 남아있는 후보자의 득표율이 모두 같은 경우, 투표 끝
		if (max == min) {
			for (int i : remains) {
				System.out.println(candidates[i]);
			}
			return true;
		}
		
		// 남아있는 후보자가 2명 이상이며, 50% 이상 득표한 후보자가 있는 경우, 투표 끝
		if (remains.size() >= 2 && max * 2 >= v) {
			for (Entry<Integer, Integer> entry : entrySet) {
				if (entry.getValue() == max) {
					System.out.println(candidates[entry.getKey()]);
					break;
				}
			}
			return true;
		}
		
		// 그 외에는 당선된 후보가 없으므로, 가장 적은 득표수를 얻은 후보자 탈락
		for (Entry<Integer, Integer> entry : entrySet) {
			if (entry.getValue() == min) {
				remains.remove(entry.getKey());
				for (List<Integer> vote : votes) {
					vote.remove(entry.getKey());
				}
			}
		}
		return false;
	}
}
