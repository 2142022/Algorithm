from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # head를 복사한 연결리스트
        h = head

        # 연결리스트의 노드를 큐에 담기
        q = deque()
        while h:
            q.append(h.val)
            h = h.next
        
        # 큐의 앞과 뒤를 한번씩 연결리스트에 연결하기
        while q:
            # 큐의 앞의 원소 추가
            head.val = q.popleft()
            head = head.next

            # 큐에 원소가 있다면 뒤의 원소 추가
            if q:
                head.val = q.pop()
                head = head.next
