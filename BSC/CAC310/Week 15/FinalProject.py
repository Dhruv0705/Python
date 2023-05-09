class Node:
    def __init__(self, value=None, prev=None, next=None, data=None):
        self.value = value
        self.prev = prev
        self.next = next
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def insert(self, value, position):
        if position < 0 or position > self.size:
            raise ValueError("Invalid position")
        
        new_node = Node(value)
        
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        elif position == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif position == self.size:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            current_node = self.head
            for i in range(position-1):
                current_node = current_node.next
            new_node.prev = current_node
            new_node.next = current_node.next
            current_node.next.prev = new_node
            current_node.next = new_node
            
        self.size += 1
        self.print_list()
        
    def delete(self, position):
        if position < 0 or position >= self.size:
            raise ValueError("Invalid position")
        
        if self.size == 1:
            self.head = None
            self.tail = None
        elif position == 0:
            self.head = self.head.next
            self.head.prev = None
        elif position == self.size-1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current_node = self.head
            for i in range(position-1):
                current_node = current_node.next
            current_node.next = current_node.next.next
            current_node.next.prev = current_node
            
        self.size -= 1
        self.print_list()
        
    def add_first(self, value):
        self.insert(value, 0)
        
    def add_last(self, value):
        self.insert(value, self.size)
        
    def get(self, position):
        if position < 0 or position >= self.size:
            return None
        
        current_node = self.head
        for i in range(position):
            current_node = current_node.next
        return current_node.data
        
    
    def deep_copy(self):
        new_list = DoublyLinkedList()
        current_node = self.head
        while current_node:
            new_list.add_last(current_node.value)
            current_node = current_node.next
        return new_list
    
    def get_size(self):
        return self.length
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" ")
            current_node = current_node.next
        print()
        
def main():
    linked_list = DoublyLinkedList()

    while True:
        print("Select an option:")
        print("a. Insert")
        print("b. Delete")
        print("c. Add first")
        print("d. Add last")
        print("e. Get")
        print("f. Deep copy")
        print("g. Size")
        print("h. Exit")

        choice = input("> ")

        if choice == "a":
            val = int(input("Enter value to insert: "))
            pos = int(input("Enter position to insert: "))
            linked_list.insert(val, pos)
            linked_list.print_list()

        elif choice == "b":
            pos = int(input("Enter position to delete: "))
            linked_list.delete(pos)
            linked_list.print_list()

        elif choice == "c":
            val = int(input("Enter value to add to the beginning: "))
            linked_list.add_first(val)
            linked_list.print_list()

        elif choice == "d":
            val = int(input("Enter value to add to the end: "))
            linked_list.add_last(val)
            linked_list.print_list()

        elif choice == "e":
            pos = int(input("Enter position to get: "))
            node = linked_list.get(pos)
            if node:
                print(f"Value at position {pos}: {int(node)}")
            else:
                print("Invalid position")
        
        elif choice == "f":
            copy_list = linked_list.deep_copy()
            print("Original linked list:")
            linked_list.print_list()
            print("Copied linked list:")
            copy_list.print_list()
            print(f"Original list name: {linked_list}")
            print(f"Copied list name: {copy_list}")
            print(f"Original list pointer location: {id(linked_list)}")
            print(f"Copied list pointer location: {id(copy_list)}")

        elif choice == "g":
            print(f"Size of linked list: {int(linked_list.get_size)}")

        elif choice == "h":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

'''
Report:	
Please	include	a	short	report	consisting	of	the	following	information.	
• What	language	did	you	choose	to	implement	the	program	in	and	why?
    Python because it is easy to use and understand.

• Formally	describe	the	language	(generation,	paradigm,	compiled	vs.	
interpreted,	etc.).	Did	any	of	these	features	influence	your	language	choice?
    Generation: 4th generation
    Paradigm: Object-oriented, imperative, functional, procedural, reflective
    Compiled vs. interpreted: Interpreted
    These features did not influence my language choice.

• Briefly	describe	the	logic	behind	your	program.	How	did	you	approach	the	
problem?	Highlight	any	areas	that	were	particularly	difficult	or	that	you	are	
proud	of.	
    I approached the problem by using the doubly linked list data structure.
    I mainly used the code from the java doubly linked list code and converted it to python from last semester.
    I did had to add and implement new feature in where I did google the deep copy method and implemented it.
    I also implement a while loop to keep the program running until the user enters h to exit the program.
    Other than that I did not have any difficulties as the code was very similar to the java program that I still kept. 

• Reflection	about	the	course:	do	you	think	you	learned	something	new	in	this	
course?	Did	the	course	content	push	you	to	think	more	critically?	Did	any	
portion	of	the	course	aid	in	your	ability	to	complete	the	final	project?	
Constructive	criticism	is	always	welcome.
    I did learn something new in this course. I learned about different programming language and i learned the fundamental of them all.
    The course did push me to think more critically.
    The course content did aid in my ability to complete the final project.
    No the course was great and I enjoyed it.
    Thank You for everything!
'''


    
   
