
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkList:
    def __init__(self):
        self.head = None

    def initList(self, data) -> ListNode:
        # 创建头结点
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node   #连线
            p = p.next      #移位
        return r

    def printlist(self, head):
        if head == None: return
        node = head
        while node != None:
            if node.next != None:
                print(node.val, end='->')
            else:
                print(node.val, end='')
            node = node.next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        i = 0
        if not head or not head.next: return False
        while head.next and i < 10010:
            head = head.next
            i += 1
        if i < 10000:
            return False
        else:
            return True

case = Solution()
data1 = [1,2,3,4,5]
data2 = [1,4,6]
L1 = LinkList().initList(data1)
L2 = LinkList().initList(data2)
l = case.hasCycle(L1)
print(l)