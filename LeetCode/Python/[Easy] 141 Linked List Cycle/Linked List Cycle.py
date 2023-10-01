# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 연결 리스트를 하나씩 모두 탐색하는 포인터와 한 칸 건너뛰며 탐색하는 포인터 이용
        # 순환되는 곳이 있다면 언젠가는 만나게 돼있음

        # 연결 리스트를 하나씩 모두 탐색할 때의 포인터
        p1 = head
        # 연결 리스트를 한 칸 건너뛰며 탐색할 때의 포인터
        p2 = head

        while p2 and p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next

            # 두 포인터가 같다면 순환 존재
            if p1 == p2:
                return True
            
        return False