from singleLinkedList import LinkedList

def printLinkedList(linkedList):
    head = linkedList.head
    while(head):
        print(head.data)
        head = head.next
def removeDuplicateFromLinkedList(linkedList):
    current = linkedList.head
    if(linkedList.head is None or linkedList.head.next is None):
        return
    hash = set()
    hash.add(linkedList.head.data)
    while(current.next is not None):
        if(current.next.data in hash):
            current.next=current.next.next
        else:
            hash.add(current.next.data)
            current=current.next
def returnKthFromLast(linkedList,k):
    current = linkedList.head
    runner = linkedList.head
    i=0
    while(runner.next is not None):
        # print("Index {} ,data {}".format(i,runner.data))
        if(i >= k):
            current = current.next
            runner = runner.next
        else:
            runner = runner.next
        i = i+1
    return current
def deleteMiddleNode(linkedList):
    current = linkedList.head
    runner = linkedList.head
    temp = linkedList.head
    while( runner.next is not None):
        if(runner.next.next is None):
            break
        runner = runner.next.next
        temp = current
        current=current.next
    nodeToBeDeletedReference = current.next
    temp.next = nodeToBeDeletedReference
if __name__ =='__main__':
    listOfValues = [1,2,2,4,4,5,6,6,6,6,4,4,4,1,1]
    listOfValues_2 = [1,2,3,4]
    linkedList = LinkedList()

    linkedList.createLinkedListByArray(listOfValues_2)
    # removeDuplicateFromLinkedList(linkedList)
    # printLinkedList(linkedList)
    kthLinkedList = returnKthFromLast(linkedList,5)
    deleteMiddleNode(linkedList)
    # print(kthLinkedList.data)
    printLinkedList(linkedList)

