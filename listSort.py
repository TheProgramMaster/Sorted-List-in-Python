#Initializes empty list with one variable of null value
myList = [0]
#Initializes initial empty list size
index = 0
#Continually requests user to enter new value into ever-expanding list.
#Pops last value in list when user enters sentinal value to exit loop,
#Thereby removing the null value added at end of list by default.
while(True):
    val = int(input("Please enter a value (-1 to quit) as an integer: "))
    if(val == -1):
        myList.pop(len(myList)-1)
        break
    myList[index] = val
    index += 1
    newLength = len(myList)+1
    newList = [0]*newLength
    for i in range(len(newList)-1):
        newList[i] = myList[i]
    myList = newList
    
#Prints list in unsorted form
print("Value of List in Unsorted Form: " + str(myList))

#Initializes empty list that is to act as sorted version of original list.
sortedList = [0]*len(myList)
#Determines minimum value of list in each iteration of for loop,
#assigns value of index of iteration of sorted list to minimum value,
#then removes minimum value from original list, thereby rendering a sorted
#list at the end of the loop execution
for i in range(len(myList)):
    minVal = min(myList)
    sortedList[i] = minVal
    myList.remove(minVal)

#Prints list in sorted form
print("Value of List in sorted Form: " + str(sortedList))
    
