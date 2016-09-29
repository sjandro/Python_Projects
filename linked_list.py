class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def insert(self, x):
        if self.head == None:
            self.head = Node(x, None)
            self.last = self.head
        elif self.last == self.head:
            self.last = Node(x, None)
            self.head.set_next_node(self.last)
        else:
            current = Node(x, None)
            self.last.set_next_node(current)
            self.last = current

    def get_list_size(self):
        count = 0
        position = self.head
        while position:
            count += 1
            position = position.get_next_node()
        return count

    def returnHead(self):
        return self.head

    def search(self, data):
        position = self.head
        found = False
        while position and found is False:
            if position.get_data() == data:
                found = True
            else:
                position = position.get_next_node()
        if position == None:
            raise ValueError("Data not found")    
        return position

    def delete(self, data):
        position = self.head
        previous = None
        found = False
        while position and found is False:
            if position.get_data() == data:
                found = True
            else:
                previous = position
                position = position.get_next_node()

        if position == None:
            raise ValueError("Data not found")
        if previous is None:
            self.head = position.get_next_node()
        else:
            previous.set_next_node(position.get_next_node())

def print_list(head):
    position = head
    while position:
        print(str(position.get_data()))
        position = position.get_next_node()

def mergeLinkedLists(head_one, head_two):
    dummy = Node(0)
    pointer = dummy
    while head_one !=None and head_two !=None:
        if head_one.get_data()<head_two.get_data():
            pointer.set_next_node(head_one)
            head_one = head_one.get_next_node()
        else:
            pointer.set_next_node(head_two)
            head_two = head_two.get_next_node()
        pointer = pointer.get_next_node()

    if head_one == None:
        pointer.set_next_node(head_two)
    else:
        pointer.set_next_node(head_one)
    return dummy.get_next_node()

def removeGreaterThan(head, x):
    dummy = Node(0)
    pointer = dummy
    count = 0
    
    while head != None:
        if head.get_data() > x:
            pass
        else:
            pointer.set_next_node(head)
            pointer = pointer.get_next_node()
        head = head.get_next_node()
        pointer.set_next_node(None)
    return dummy.get_next_node()

def insertToTail(head, data):
    dummy = Node(0)
    pointer = dummy

    while head != None:
        pointer.set_next_node(head)
        head = head.get_next_node()
        pointer = pointer.get_next_node()
    pointer.set_next_node(Node(data))
    
    return dummy.get_next_node()

def insertToHead(head, data):
    if head == None:
        head = Node(data)
        return head
    else:
        newHead = Node(data, head)
        return newHead

def InsertNth(head, data, position):
    if head == None:
        head == Node(data)
        return head
    else:
        count = 0
        dummy = Node(0)
        current = dummy
        prev = None
        
        while head != None:
            if count == position+1 and prev != None:
                prev.next_node = Node(data,current)
                current = Node(data, head.next_node)
                break
            elif count == position+1 and prev == None:
                current = Node(data, head.next_node)
                break
            else:
                count += 1
                current.next_node = head
                prev = current
                current = current.next_node
                head = head.next_node
        return dummy.next_node

def main():
    linkedList = LinkedList()
    
    for i in range(0,10):
        linkedList.insert(i)

    print("LinkedList One before deletion:")
    print_list(linkedList.returnHead())

    for i in range(linkedList.get_list_size()):
        if linkedList.search(i).get_data() % 2 == 0:
            linkedList.delete(i) 

    print("")
    print("LinkedList One after deletion:")
    print_list(linkedList.returnHead())

    linkedList2 = LinkedList()

    for i in range(0,15):
        if i % 2 == 0:
            linkedList2.insert(i)

    print("")
    print("LinkedList Two:")
    print_list(linkedList2.returnHead())

    mergedListHeadNode = mergeLinkedLists(linkedList.returnHead(), linkedList2.returnHead())

    print("")
    print("Merged LinkedList:")
    print_list(mergedListHeadNode)

    print("")
    print("Removed values greater than 5:")
    nL = removeGreaterThan(linkedList.returnHead(),5)
    print_list(nL)

    print("")
    print("Insert 13:")
    nL2 = insertToTail(nL, 13)
    print_list(nL2)

    print("")
    print("Insert new head 123:")
    nL3 = insertToHead(nL2, 123)
    print_list(nL3)

    print("")
    nth = 5
    print("Insert to  "+str(nth)+" position:")
    nL4 = InsertNth(nL3, 32432 ,nth)
    print_list(nL4)


main()

