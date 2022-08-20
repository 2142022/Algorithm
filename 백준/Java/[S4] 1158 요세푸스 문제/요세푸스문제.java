import java.util.Scanner;

//노드 클래스
class Node {
	public int pNum; // 사람 번호
	public Node link; // 다음 노드 가리킴

	public Node(int pNum) {
		this.pNum = pNum;
		this.link = null;
	}
}

//원형 큐 클래스
class LinkedQueue {
	private Node front; // 큐의 첫번째 노드
	private Node rear; // 큐의 마지막 노드
	private int size; // 큐 사이즈

	// 큐 생성자
	public LinkedQueue() {
		this.front = null;
		this.rear = null;
		this.size = 0;
	}

	public Node getFront() {
		return front;
	}

	public void setFront(Node front) {
		this.front = front;
	}

	public Node getRear() {
		return rear;
	}

	public void setRear(Node rear) {
		this.rear = rear;
	}

	public int getSize() {
		return size;
	}

	public void setSize(int size) {
		this.size = size;
	}

	// 큐가 공백상태인지 확인
	public boolean isEmpty() {
		return ((front == null) && (rear == null));
	}

	// 마지막에 노드 삽입
	public void enQueue(int pNum) {
		Node node = new Node(pNum); // 새로운 노드 생성
		size++;

		// 큐가 공백인 경우와 그렇지 않은 경우
		if (isEmpty()) {
			front = node;
			rear = node;
		} else {
			rear.link = node;
			rear = node;
			rear.link = front;
		}
	}

	// 첫번째 노드 삭제
	public int deQueue() {
		if (isEmpty()) {
			return -1;
		}

		size--;

		// 큐에 노드가 1개 남아있는 경우
		if (front.link == null) {
			Node result = front;
			front = null;
			rear = null;
			return result.pNum;
		} else {
			Node result = front;
			front = result.link;
			rear.link = front;
			return result.pNum;
		}
	}
}

public class 요세푸스문제 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();

		int N = sc.nextInt(); // 전체 사람의 수
		int K = sc.nextInt(); // K번째 사람 제거

		// 큐 생성
		LinkedQueue person = new LinkedQueue();

		// 큐에 사람 저장
		for (int i = 1; i <= N; i++) {
			person.enQueue(i);
		}

		sb.append("<");

		int i = 1;
		while (person.getSize() > 1) {
			// K번째 사람 제거
			if (i % K == 0) {
				sb.append(person.deQueue());
				sb.append(", ");
			}
			// 그 외에는 front와 rear를 옮기기
			else {
				person.setFront(person.getFront().link);
				person.setRear(person.getRear().link);
			}
			i++;
		}

		// 마지막 사람 제거
		sb.append(person.deQueue());

		sb.append(">");

		System.out.println(sb);
	}
}