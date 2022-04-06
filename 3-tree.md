# Binary Search Tree
## What is it?
This is a tree:

![My image file](https://github.com/EmmaBurkett/CSE212-final-project/blob/main/hidden_files/Capture.PNG)

A tree is connected like a linked list, except each node has three nodes attached to it unless it's the head or one of the tails. On each node there is a left and a right, the left stores a node with a number lower than the current node and the right stores a node with a number higher than the current node.

### self.tail
Also unlike a linked list a tree does not store it's tail(s) in another class. That means that to access each tail you need to iterate through the elements above it which can give O(1) time to O(n) time. 

## Balanced Binary Search Tree


## Operation Performance

Operation     | Description       | Python Code | Performance 
--------------|-------------------|-------------|-------------
add(value)| Adds value to the set    | my_set.add(value)   | O(1)
remove(value)     | Removes the value from the set     | my_set.remove(value)   | O(1)
member(value)        | Determines if value is in the set | if value in my_set | O(1)
size()       | Returns the number of items in the set | length = len(my_set) | O(1)

## Dice Game
In the 30's dice game if the player rolls two of the same number they
get a point. 

Using the previous tutorial's code we have added a new method: check _uniqueness

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

        # Add points if there are two of the same number dice. 
        self.check_uniqueness()

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

    def check_uniqueness(self):

        # Initialize the set.
        my_set = set()

        # Loop through the array.
        for die in self.dice:

            # Check if the die is in the set - O(1) operation.
            if die in my_set:

                # If die in set then add a point to the score
                self.score += 1
            
            # Add die after checking if the value is in set.
            my_set.add(die)
        

game = DiceGame()
game.start_game()
```
## Coding with sets
In the check_uniqueness method we turned an array into a set. This helped us
to check the dice for uniqueness in O(1) time. This is a huge advantage over
arrays as ``` If die in array ``` is O(n) time. 


## Coding Challenge: 
Alter the check_uniqueness method to ingnore a third or fourth duplicate dice
by using chaining. 


