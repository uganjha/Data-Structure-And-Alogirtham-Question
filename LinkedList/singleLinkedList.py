class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,node):
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = node
        else:
            self.head = node
    def createLinkedListByArray(self,listOfArray):
        if(len(listOfArray) <= 0):
            raise Exception("Should be a list with minimum length greater than 0")

        for i in  range(0,len(listOfArray)):
            # print(listOfArray[i])
            node = Node(listOfArray[i])
            self.insert(node)
    def deleteLinkedListByPosition(self,position):
        i = 0
        head = self.head
        if(self.head == None):
            return
        if(position == 0):
            self.head = head.next
            return
        for i in range(0,position - 1):
            head = head.next
            if(head is None):
                break
        if(head is None or head.next is None):
            return
        temp = head.next.next
        head.next = temp
        
    def deleteLinkedListByValue(self,value):
        head = self.head
        if(head.data == value):
            self.head = head.next
        while(head.next):
            if(head.next.data == value):
                head.next = head.next.next
            head = head.next
        return
        
# class createLinkedList:
#     def joinLinkList(self,firstLinkedList,secondLinkList,position):

#     def deleteLinkedList(self,linkedList,position):
    
#     def insertLinkedList(self,linkedList,position)

#     def createLinkedListByArray(self,listOfArray):
#         if(len(listOfArray) <= 0):
#             raise Exception("Should be a list with minimum length greater than 0")
#         linkedList = self.createHead(listOfArray[0])
#         head 
#         for i in  range(1,len(listOfArray)-1):

            