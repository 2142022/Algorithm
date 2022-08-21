import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class 종이자르기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 종이의 가로와 세로의 길이
		int row = sc.nextInt();
		int col = sc.nextInt();

		// 자르는 횟수
		int cnt = sc.nextInt();

		// 가로로 자를 때의 인덱스
		List<Integer> rCut = new ArrayList<>();
		rCut.add(0);
		rCut.add(col);

		// 세로로 자를 때의 인덱스
		List<Integer> cCut = new ArrayList<>();
		cCut.add(0);
		cCut.add(row);

		// 자르는 인덱스 입력받기
		for (int i = 0; i < cnt; i++) {
			int op = sc.nextInt();

			// 가로
			if (op == 0) {
				rCut.add(sc.nextInt());
			}

			// 세로
			else {
				cCut.add(sc.nextInt());
			}
		}

		// rCut, cCut 오름차순 정렬
		Collections.sort(rCut);
		Collections.sort(cCut);
		
		// 잘린 종이 중 가로 길이의 최대값
		int w = 0;
		for (int i = 1; i < cCut.size(); i++) {
			w = Math.max(w, cCut.get(i) - cCut.get(i - 1));
		}

		// 잘린 종이 중 세로 길이의 최대값
		int h = 0;
		for (int i = 1; i < rCut.size(); i++) {
			h = Math.max(h, rCut.get(i) - rCut.get(i - 1));
		}

		// 출력
		System.out.println(w * h);
	}
}
