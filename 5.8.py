class Queue:
    def _init_(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue.")
        else:
            removed_item = self.queue.pop(0)
            print(f"Dequeued: {removed_item}")
    
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue:", self.queue)
    
def menu():
    print("Queue Menu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display Queue")
    print("4. Exit")

def main():
    q = Queue()
    
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            item = int(input("Enter item to enqueue: "))
            q.enqueue(item)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if _name_ == "_main_":
    main()
