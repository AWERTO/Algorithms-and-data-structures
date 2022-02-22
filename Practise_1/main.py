from myPackage.LinkedList import LinkedList
# At this point the list is empty
listOfNumbers = LinkedList()

# Adding the first node to the list
listOfNumbers.append( 5 )
listOfNumbers.append( 8 )
listOfNumbers.append( 10 )
listOfNumbers.append( 2 )
listOfNumbers.append( 1 )
listOfNumbers.append( 3 )
listOfNumbers.reverseNode()
listOfNumbers.deleteHead()
listOfNumbers.prepend( 4 )
listOfNumbers.printList()