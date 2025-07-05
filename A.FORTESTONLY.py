
class Node:
    def __init__(self,v):
        self.val = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self,v):
        newnode = Node(v)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
    
    def add_to_head(self,v):
        ...

    def delete(self,v):
        if self.head is None:
            return "Blankkk"
        p = self.head
        if p.val==v:
            self.head=p.next
            return "Succeeded"
        while p.next is not None:
            # check
            follow=p
            p=p.next
            if p.val==v:
                follow.next=p.next
                return "Succeeded"
        return f"What the hell you make me search smth that does not exist you notherducker"

    def __str__(self):
        ans = ""
        p = self.head
        while p is not None:
            ans = ans + str(p.val) + " "
            p = p.next
        return ans
    


LL = LinkedList()
print(LL)