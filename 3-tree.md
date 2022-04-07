# Tree
## What is it?
This is a tree:

![My image file](https://github.com/EmmaBurkett/CSE212-final-project/blob/main/hidden_files/Capture.PNG)

A binary tree is a data structure made up of instances of a class which are connected like a linked list. The difference between a tree and a linked list is that each node can point to two new nodes, and does not point to the previous node. 

## Binary Search Tree
A binary serach tree is specific in how it links together. Observe the image above. Nodes with values 3 and 5 point to two new nodes. In both cases the node with the larger value is placed on the right of the current node (6 is to the right of 5), and the node with the smaller value is placed on the left of the current node (4 is to the left of 5).

Another integral part of a BST is that a number greater than the current node cannot be placed left of the tree and a number less than the current node cannot be place on the right of the tree. 

Observe from the image above that a number greater than 3 cannot be found on the left of the node and a node less than 3 cannot be found on the right of the node.

The benifit to BST is that we can search through the data structure in 
O(tree.height). 

Note:
Unlike a linked list, a tree does not store it's tail(s) in another class. That means that to access each tail you need to iterate through the nodes above it which can give O(1) time to O(n) time. 

## Balanced Binary Search Trees
Because a Binary Search tree can have a height equal to it's number of nodes it can take O(n) time to get to the node on the end. If the tree is 'balanced' or the height of any two subtrees is reasonably similar then it only takes O(log n) time to access the nodes on the end or to find a specific node. 

![My image file](https://github.com/EmmaBurkett/CSE212-final-project/blob/main/hidden_files/image.PNG)

## Searching by O(log n)
Observe the image above. It's subtrees are of equal height, therefor it is a balanced binary search tree. If you wanted to find the node containing the value 6 you would start at the root of the tree, 5, and you would compare 5 to 6. 6 is greater than 5 so you would look to the right, eliminating all the values on the left of 5. Next you would compare 6 to 8. 6 is less than 8 so you would look to the left node, eliminating all the values on the right of 8. The final comparison, 6 vs. 7, shows that 6 is not in the tree at all. 

Note that every time we compared with a new node we halfed the amount of nodes that we needed to go through to find the node containing 6. This is the definiton of O(log n). 

## Recursion
Because each node only points to the next nodes and not the one before it is nessisary to use recursion to move backwards on the tree. When we want to print out a BST from largest to smallest we have to go to the right-most node and print out that node then the one above it. 

If we were to try to do this with a FOR loop then when we move to the right most node we don't have any connections to the node above it. 



## Operation Performance for a Balanced Binary Search Tree

Operation     | Description       | Performance 
--------------|-------------------|-------------
insert(value) | Insert a value into the tree. | O(log n) - Recursively search the subtrees to find the next available spot. 
remove(value) | Remove a value from the tree. | O(log n) - Recursively search the subtrees to find the value and then remove it. This will require some cleanup of the adjecent nodes. 
contains(value) | Determines if value is in the tree | O(log n) - Recursively search the subtrees to find the value.
traverse_forward | Visit all objects from smallest to largest | O(n) - Recursively traverse the left subtree and then the right subtree. 
traverse_reverse | Visit all objects from larges to smallest | O(n) - Recursively traverse the right subtree and then the left subtree.
height(node) | Determine the height of a node. If the height of the tree is needed, the root node is provided. | O(n) - Recursively traverse the right subtree and then the left subtree.
size() | Return the size of the BST | O(1) - The size is maintained withint the BST class. 
empty() | Returns true if the root node is empty. This can also be done by checking the size for 0. | O(1) - The comparison of the root node or the size.

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


###### Vocabulary
Term | Definition
-----|----------------------------------------------------------------
Node | An entry in a tree that contains both the value and pointers to any children nodes.
Child | A child is a node connected from a parent node.
Leaf | A leaf is a node that has no children.
Parent | A parent is a node that connects to children nodes.
Root | The first parent in a tree.
Subtree | Subset of a tree made by selecting a node to be the root and including all the children from that node. 