# Queue
## What is it?
A queue can be the same data structure as a stack except its data is accessed differently. A stack removes elements from the back of the data structure whereas a queue removes elements from the front of the data structure.

## FIFO
A queue is comparable to a line of people: If you're first in line you are the first served and the first removed from the line. This brings us to the fundamental idea behind queues:
* FIFO - First in first out.

## Practical Application
A queue should be used whenever you need to access and remove
the first element of the stack before you handle the last elements of the
stack. This can include things like handling phone calls.

## Operation Performance for an array utilizing a queue:

Operation     | Description       | Python Code | Performance 
--------------|-------------------|-------------|-------------
Enqueue(value)| Adds value to the back of the queue    | my_queue.append(value)   | O(1)
Dequeue()     | Remove and return the first item from the front of the queue.     | value = my_queue[0] or value = my_queue.pop(0)   | O(n)
size()        | Returns the size of the queue. | length = len(my_queue) | O(1)
empty()       | Returns true if length of the queue is zero. | if len(my_queue) == 0: | O(1)

## Add operation desciptions here.

## Dice Game
In the 30's dice game the player rolls six dice which are displayed
from highest to lowest. The player must keep the highest die and then 
decide if they want to keep the next highest die. 

Pay close attention to the functions enqueue_dice and dequeue_dice.

``` python
import random
class DiceGame:
    def __init__(self):
        self.dice = []
        self.score = 0
    
    def start_game(self):
        self.new_roll()
        self.get_user_input()
    
    def new_roll(self):

        # Append new values to the array.
        self.enqueue_dice()

        # Sort the array.
        self.sort_dice()

        # Display the array.
        self.display_dice()

        # Dequeue an element on the array.
        self.dequeue_dice()

        # Display the array.
        self.display_dice()

    def enqueue_dice(self):
        """This method 'rolls' the dice."""

        # Enqueue a value to an array:
        for i in range(6):
            self.dice.append(random.randint(1,6))
    
    def sort_dice(self):
        """This method sorts the dice."""

        for i in range(6):
            for j in range(i, 6):
                if self.dice[i] < self.dice[j]:
                    switch = self.dice[i]
                    self.dice[i] = self.dice[j]
                    self.dice[j] = switch

    def display_dice(self):
        """This method displays the dice to the user."""

        print(*self.dice, sep=", ")

    def dequeue_dice(self):
        """This method 'picks up' the highest die and displays it.
           It also updates the users score and displays it."""

        # Check if array is empty with the common queue operation empty() 
        if len(self.dice) == 0:
            print("No dice!")
            self.start_game()
            return

        # Dequeue() the first die in the array and display to the user.
        first_die = self.dice.pop(0)

        self.score += first_die
        print("You kept", first_die, "Your score is:", self.score)
    
    def get_user_input(self):
        """"This method asks the user if they would like to 'pick up'
            and more dice."""

        kept_die = input("Keep next die?(y/n) ")
        if kept_die == "y":
            self.dequeue_dice()
            self.display_dice()
            self.get_user_input()
        elif kept_die == "n":
            self.dice = []
            self.start_game()
        else:
            print("enter a y or a n")
            self.get_user_input(self)

game = DiceGame()
game.start_game()
```
## Coding with Queues
In the enqueue_dice method appends new values to the dice array with a
performance of O(1). The dequeue_dice method removes dice from the 
beginning of the array - which is the definition of a queue, first in;
first out.

## [Coding Challenge](https://github.com/EmmaBurkett/CSE212-final-project/blob/main/coding_challenges/dice_queue.py): 
For an array dequeuing an element is an O(n) operation, rather slow! 
This same program can be recreated with a linked list which has O(1) 
performance operations for dequeue and enqueue. 

Your challenge is to alter the enqueue_dice and dequeue_dice methods to use a linked list.

#### [Solution](https://github.com/EmmaBurkett/CSE212-final-project/blob/main/coding_challenges/Answers/dice_queue_answer.py)

