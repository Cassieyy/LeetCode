class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
class Solution:    
    def addTwoNumbers(self, l1, l2):
        val1 = 0
        val2 = 0

        cof1 = 0
        cof2 = 0
        while(l1):
            val1 += l1.val * pow(10, cof1)
            cof1 += 1
            l1 = l1.next

        while(l2):
            val2 += l2.val * pow(10, cof2)
            cof2 += 1
            l2 = l2.next
        
        val3 = val1 + val2
        head = ListNode(0)
        p = head

        while(val3 // 10):
            node = ListNode(val3 % 10)
            p.next = node
            p = p.next
            val3 //= 10
        node = ListNode(val3)
        p.next = node
        return head.next 

if __name__ == "__main__":
    l1 = [0]
    l2 = [0]
    head1 = ListNode(l1[0])
    p1 = head1
    head2 = ListNode(l2[0])
    p2 = head2

    for i in l1[1:]:
        node = ListNode(i)
        p1.next = node
        p1 = p1.next
    
    for j in l2[1:]:
        node = ListNode(j)
        p2.next = node
        p2 = p2.next
    
    # while(head1 is not None):
    #     print(head1.val)
    #     head1 = head1.next

    s = Solution()
    res = s.addTwoNumbers(head1, head2)
        
    while(res is not None):
        print(res.val)
        res = res.next

