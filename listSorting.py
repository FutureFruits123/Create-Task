def listCreator(para):
    global unsortedList
    global listLength
    listLength = para
    unsortedList = [input("What is something you want in your list?")]
    
    while listLength != len(unsortedList):
        unsortedList.append(input("What is another thing you want in your list?"))

def listSorter():
    def indexer(index):
        tempIndex = unsortedList.index(tempThing) + 1
        sortedList.insert(index, tempThing)
        print(sortedList)
        sortedList.pop(tempIndex)
        print(sortedList)
    #def correcting(index):
        #for x in unsortedList:
         #   if x == tempThing:
          #      break
        #while x != tempThing:
         #   print("The thing you entered is not in your list, try again.")
          #  tempThing = input("What is your favorite thing in your list? (Make sure capitalizations are the same)")
           # for y in unsortedList:
            #    if y == tempThing:
             #       tempIndex = unsortedList.index(tempThing) + 1
              #      sortedList.insert(index, tempThing)
               #     print(sortedList)
                #    sortedList.pop(tempIndex)
                 #   print(sortedList)
                  #  x = tempThing
    sortedList = unsortedList
    if listLength > 1:
        tempThing = input("What is your favorite thing in your list? (Make sure capitalizations are the same)")
        for x in unsortedList:
            if x == tempThing:
                indexer(0)
                break
        #correcting(0)
        while x != tempThing:
            print("The thing you entered is not in your list, try again.")
            tempThing = input("What is your favorite thing in your list? (Make sure capitalizations are the same)")
            for y in unsortedList:
                if y == tempThing:
                    tempIndex = unsortedList.index(tempThing) + 1
                    sortedList.insert(0, tempThing)
                    print(sortedList)
                    sortedList.pop(tempIndex)
                    print(sortedList)
                    x = tempThing
        if listLength > 2:
            thingsAdded = 0
            for z in unsortedList:
                thingsToBeAdded = len(unsortedList) - 2
                if thingsAdded < thingsToBeAdded:
                    tempThing = input("What is your next favorite thing in your list? (Make sure capitalizations are the same)")
                    indexer(thingsAdded + 1)
                    thingsAdded = thingsAdded + 1
                else:
                    print("Here is your ordered list: " + str(sortedList))
                    break
        else:
            print("Here is your ordered list: " + str(sortedList))
    else:
        print("Here is your ordered list: " + str(sortedList))

listCreator(int(input("How many things do you want in your list? (Enter a number)")))
listSorter()