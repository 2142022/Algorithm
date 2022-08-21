import java.util.Scanner;

public class 참외밭 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 1m^2 넓이에 자라는 참외의 개수
		int K = sc.nextInt();

		// 참외밭의 변의 방향과 길이
		int[][] field = new int[6][2];
		for (int i = 0; i < 6; i++) {
			field[i][0] = sc.nextInt();
			field[i][1] = sc.nextInt();
		}

		// 가로 길이의 최대값
		int row = 0;
		// 가로 길이 최대값의 인덱스
		int rowIdx = 0;
		// 세로 길이의 최대값
		int col = 0;
		// 세로 길이 최대값의 인덱스
		int colIdx = 0;

		for (int i = 0; i < 6; i++) {
			// 가로 길이 최대값과 인덱스 구하기
			if (field[i][0] == 1 || field[i][0] == 2) {
				row = Math.max(row, field[i][1]);
				if (row == field[i][1]) {
					rowIdx = i;
				}
			}

			// 세로 길이의 최대값과 인덱스 구하기
			else {
				col = Math.max(col, field[i][1]);
				if (col == field[i][1]) {
					colIdx = i;
				}
			}
		}

		// 전체 큰 사각형의 넓이
		int bigArea = row * col;

		// 빼야 하는 사각형의 한 변의 길이 = 가로나 세로의 최대값 양 옆에 있는 변 길이의 차
		// 빼야 하는 사각형의 세로 길이 구하기
		int colDiff;
		if (rowIdx == 0) {
			colDiff = Math.abs(field[1][1] - field[5][1]);
		} else if (rowIdx == 5) {
			colDiff = Math.abs(field[4][1] - field[0][1]);
		} else {
			colDiff = Math.abs(field[rowIdx - 1][1] - field[rowIdx + 1][1]);
		}

		// 빼야 하는 사각형의 가로 길이 구하기
		int rowDiff;
		if (colIdx == 0) {
			rowDiff = Math.abs(field[1][1] - field[5][1]);
		} else if (colIdx == 5) {
			rowDiff = Math.abs(field[4][1] - field[0][1]);
		} else {
			rowDiff = Math.abs(field[colIdx - 1][1] - field[colIdx + 1][1]);
		}

		// 빼야 하는 사각형의 넓이
		int smallArea = rowDiff * colDiff;

		System.out.println((bigArea - smallArea) * K);
	}
}
