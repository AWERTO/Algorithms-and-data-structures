from myPackage.Node import Node

class LinkedList:
    def __init__( self ):
        self.head = None
        self.tail = None
    
    
    
    def printList( self ):
        current = self.head
        while current != None:
            print( current.val )
            current = current.next

    def prepend( self, val ):
        newNode = Node( val )
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def append( self, val ):
        newNode = Node( val )
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode


    def deleteNode( self, val ):
        if self.head == None:
            return None
        current = self.head
        previous = self.head
        if self.head.val == val:
            self.head = self.head.next
            current.next = None
        else:
            while current != None and current.val != val:
                previous = current
                current = current.next
            if current != None:
                previous.next = current.next
                current.next = None

    def findNode( self, val ):
        current = self.head
        while current != None:
            if current.val == val:
                return current
            current = current.next
        return None

    def deleteTail( self ):
        if self.tail !=  None:
            return None
        
        deletedTail = self.tail
        if self.head == deletedTail:
            self.head = None
            self.tail = None

        currentNode = self.head
        while (currentNode.next):
            if currentNode.next.next != None:
                currentNode.next = None
            else:
                currentNode = currentNode.next

        self.tail = currentNode
        return deletedTail

    def deleteHead( self ):
        if self.head == None:
            return None
        
        deletedHead = self.head
        if self.head.next != None:
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None

        return deletedHead
        

    def length( self ):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def fromArray( self, index, val ):
        newNode = Node( val )
        if index <= self.length():
            if index == 0:
                self.append( val )
            else:
                count = 0
                current = self.head
                while count < index - 1:
                    count += 1
                    current = current.next
                newNode.next = current.next
                current.next = newNode

    def toArray( self ):
        nodes = []
        currentNode = self.head
        while currentNode != None:
            nodes.push(currentNode)
            currentNode = currentNode.next

        return nodes

    def toString( self ):
        nodes = ""
        currentNode = self.head
        while currentNode != None:
            nodes += currentNode.next

        return nodes
    
    def reverseNode( self ):
        currentNode = self.head
        previousNode = None
        nextNode = None
        while currentNode != None:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode

        self.head = previousNode
