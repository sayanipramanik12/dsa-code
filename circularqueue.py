from array import *
import os

size = 5    # Maximum numbers to be stored in the array. We can increase the quantity by changing the value 5 with a new one
arr = array('i',[])     # An empty array for queue implementation
R = -1
F = 0
te = 0

# Initilise the array with 0
for i in range(0,size):
    arr.append(0)


while 1:    # An infinite while loop
    os.system('cls')    # Clear the console screen in Windows OS. For Linux and MacOS use os.system('clear')
    print('1. Add')
    print('2. Delete')
    print('3. Display')
    ch=int(input('Enter your choice '))

    if ch==1:
        # Check if the queue is full
        if te==size:
            print('Queue is full')
            input('Press enter to continue...')     # Pause the loop so that the user can see the above message Queue is full
        else:
            # If queue is not full then append the number in the array
            n=int(input('Enter a number '))
            R=(R+1)%size
            arr[R]=n
            te = te + 1

    elif ch==2:
        # Check if the queue is empty
        if te==0:
            print('Queue is empty')
            input('Press enter to continue...')     # Pause the loop so that the user can see the above message Queue is empty
        else:
            # If queue is not empty then remove the number at index 0 from the array
            print('Number Removed = %d' %(arr[F]))
            F=(F+1)%size
            te = te - 1
            input('Press enter to continue...')     # Pause the loop so that the user can see the above message Number Removed = ?

    elif ch==3:
        # Check if the queue is empty
        if te==0:
            print('Queue is empty')
            input('Press enter to continue...')     # Pause the loop so that the user can see the above message Queue is empty
        else:
            # if queue is not empty then display all the number
            x = F
            for i in range(1,te+1):
                print(arr[x], end=' ')
                x=(x+1)%size
            input('\nPress enter to continue...')     # Pause the loop so that the user can see full queue on the screen
    else:
        print('Invalid Choice')
        input('Press enter to continue...')     # Pause the loop so that the user can see the above message Invalid Choice
