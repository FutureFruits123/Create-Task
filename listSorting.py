def listCreator(para):
    global unsortedList
    global listLength
    listLength = para
    unsortedList = [input("What is something you want in your list?")]
    
    while listLength != len(unsortedList):
        unsortedList.append(input("What is another thing you want in your list?"))

    return unsortedList

def listSorter():
    sortedList = unsortedList
    if listLength > 1:
        print(unsortedList)
        favItem = input("What is your favorite thing that is in your list? (Make sure capitalizations are the same)")
        for x in unsortedList:
            if x == favItem:
                favIndex = unsortedList.index(favItem) + 1
                sortedList.insert(0, favItem)
                sortedList.pop(favIndex)
                break
        if x != favItem:
            print("uh oh")
    else:
        print("Here is your ordered list: " + str(sortedList))

listCreator(int(input("How many things do you want in your list? (Enter a number)")))
listSorter()