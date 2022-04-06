# Set
## What is it?
A set is an ordered list. In an array elements are appended to the end
of the array or inserted into the middle or beginning. With sets elements
are added to the location on the array that they represent. For example
if you want to add 5 to a set you would do this: my_set[5] = 5
Note that the index matches the value of the element. 

### Example:
``` python
array = [1,4,3]
my_set = [None, 1, None, 3, 4,]
```

### Advantages
Note in the example above that a set only has one index equal to four
meaning that we can't have another four in our set without working around
the set. This can be an advantage because we can use it to check for 
uniquness.

### Iterate through a set
You can't iterate through a set. But you can use a foreach loop to loop through a set:
```python
add = 0
for x in my_set:
    add += x
print(add)
```

### Add Hashing here

## Practical Application
Sets can be used to verify uniquness which can be useful if you have a 
list of employees and you need to make sure that their ID numbers are 
unique from everyone else's numbers. Sets can also be used if you need
to be able to find values quickly. To check if a set has a value is O(1)
performance time because the value is used as the index into the set and
if there is a value in that location then the set has the value. 

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

Using the queue tutorial's code we have added a new method: check _uniqueness

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


## [Coding Challenge](CSE212-final-project\coding_challenges\dice_set.py): 
Right now the check_uniqueness method gives a point for every additional
die with the same number - so if you rolled four 5's it would award the
user with 3 points. Alter the check_uniqueness method so it awards one point
for each pair of duplicate dice. Ex. if you rolled four 5's it would 
give the user 2 points. 

You cannot use a counter to solve this problem. 
#### [Solution](CSE212-final-project\coding_challenges\Answers\dice_set_answer.py)


