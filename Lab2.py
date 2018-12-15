'''
Data Structures(CS2302)
Lester Ibarra
LAB2: PASSWORDS
Aguirre, Diego
Nath, Anindita
This lab will be able to determine the TOP 20 most used passwords based
on the text file "test.txt" by using merge and bubble sort
'''
class Node(object):#The following is the standard code for Node Class

    #Constructor
    def __init__ (self,password,count,next = None):
        self.password = password
        self.count = count
        self.next = next

    #setters
    def setPassword(self, password):
        self.password = password
    def setCount(self, count):
        self.count = count
    def setNext(self, next):
        self.next = next

    #getters
    def getPassword(self):
        return self.password
    def getCount(self):
        return self.count
    def getNext(self):
        return self.next


class LinkedList(object):#The following is the standard code for linked lists

    #method to create head of linked list
    def __init__(self, head = None):
        self.head = head

    #method to insert items into the linked list
    def insert(self, password, count):
        newNode = Node(password, count)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    #method to compare nodes in the link list and create a link list with no repeated nodes
    def compare(self, password, count):
        current = self.head
        repeat = False
        while current and repeat is False:
            if current.getPassword() == password:
                current.setCount(current.getCount() + 1)
                repeat = True
            else:
                current = current.next

        if current is None:
            return 1

    #method to determine the size of the linked list, it was not needed but i added it just in case
    def size(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.getNext()
        return size

    #method to print link list
    def printList(self):
        temp = self.head
        while temp:
           print("Password: %s Count: %d" % (temp.password, temp.count))
           temp = temp.next
           

    #method to print link list of top 20 count nodes
    def printTop20(self):
        temp = self.head
        for i in range(20):
            if temp == None:
                print
            print("Password: %s Count: %d" % (temp.password, temp.count))
            temp = temp.next
    
    
#method that goes through a txt file and only adds lines that do no repeat
def trim():#lab solution A
    Password_List = LinkedList()
    empty = True
    with open("test.txt", "r") as file:
        for line in file:
            try:
                if empty == True:
                    Password_List.insert(line.split()[1], 0)
                    empty = False
                result = Password_List.compare(line.split()[1], 1)
                if result == 1:
                    Password_List.insert(line.split()[1], 1)
                #exception to protect against skipped lines
            except IndexError:
                pass
            continue
    return Password_List

#method to sort the list by count values
def Bubble_Sort(self):
     if self.head == None:
         return
     #loop to compare count of next node and keep checking until None is reached
     for i in range(self.size()):
         #loop repeats the size of the list
        temp = self.head
        while temp.next is not None:
            if temp.getCount() < temp.next.getCount():
                tempCount, tempPassword = temp.getCount(), temp.getPassword()
                temp.setCount(temp.next.getCount())
                temp.setPassword(temp.next.getPassword())
                temp.next.setCount(tempCount)
                temp.next.setPassword(tempPassword)
            temp = temp.next

#method to read a file and use a dictionary to count the number of repetitions
def DictionaryRead():#solution B for lab
    #key list
    password_dict = {}
    passwordList = LinkedList()
    #loop to go through the txt file
    with open("password.txt", "r") as file:
        for line in file:
            try:
                current_line = line.split()[1]
                if current_line in password_dict:
                    password_dict[current_line] = password_dict[current_line] + 1
                else:
                    password_dict[current_line] = 1
            except IndexError:
                pass
        #loop to populate linked list
    for item, i in password_dict.items():
        passwordList.insert(item, i)
    return passwordList

#methof to sort linked list using merge Sort
def Merge_Lists(left, right):
    if left is None:
        return right
    if right is None:
        return left
    #recursive calls to merge lists in the correct order
    if left.getCount() >= right.getCount():
        temp = left
        temp.next = Merge_Lists(left.next, right)
    else:
        temp = right
        temp.next = Merge_Lists(left, right.next)
    return temp

#Defining function which will sort the linked list using mergeSort
def Merge_Sort(head):
    #base case
    if head is None or head.next is None:
        return head
    #method call to split left and right
    left, right = divideLists(head)
    #sort node
    left = Merge_Sort(left)
    right = Merge_Sort(right)
    #merge left and right node
    head = Merge_Lists(left,right)
    return head

#find mid and split list using slow fast
def divideLists(head):
    #varibles to track position
    slow = head
    fast = head

    if fast:
        fast = fast.next
    #loop to find mid by moving position of fast slow
    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next
    mid = slow.next
    slow.next = None
    return head, mid

#main method
def main():
    print("**********SOLUTION A**************\n")

    #Solution A
    Password_List = trim()#This will avoid including duplicates 
    #sort method is called
    Bubble_Sort(Password_List)
    Password_List.printTop20()#print top 20 occurrences

    #Solution B
    print("**********Solution B**************\n")
    #create linked list using dictionary
    Dict_List = DictionaryRead()
    #sort dictionary list using merge sort
    Merge_Sort(Dict_List.head)
    #print top 20 occurrences in dictionary list
    Dict_List.printTop20()

main()