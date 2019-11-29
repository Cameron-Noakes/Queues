# Queue
# 2 pointers
# FIFO
# Circular data structure
# Reduce the need for global variables
#Non- primitive

pointer_start = 0
pointer_end = 0
queue = []
state = True


def enqueue():
    global pointer_start
    global pointer_end
    global queue
    add_item = True
    
    while add_item == True:
        add = input("Enter the items you would like to add (0 to end): ")
        queue.append(add)
        pointer_end += 1
        if add == "0":
            add_item = False
            queue.pop()
            pointer_end = pointer_end - 2
            print ("Items added to queue.\npointer at start = ",pointer_start,"\npointer at end = ",pointer_end,"\n")
            return pointer_end
    
        

def dequeue():
    global pointer_start
    global pointer_end
    global queue
    print ("queue:",queue)
    popping = input("Would you like to pop? (y/n): ")
    if popping == "y":
        print (queue.pop(0))
        print ("Queue after popping: ",queue)
        print ("pointer at start = ",pointer_start, "\npointer at end = ",pointer_end-1,"\n")

    elif popping == "n":
        __main__()

    elif pointer_end == 0:
        print ("Queue is empty.")
        __main__()
        



def read():
    print ("Queue:",queue,"\nstart pointer:",pointer_start,"end pointer:",pointer_end,"\n")
    __main__


def __main__():
    
    

    choice = input("Enter a function of enqueue, dequeue or read (e,d,r)")

    if choice == "e":
        enqueue()

    elif choice == "d":
        dequeue()

    elif choice == "r":
        read()

    else:
        print ("Please enter a valid option.")

while state == True:
    __main__()

