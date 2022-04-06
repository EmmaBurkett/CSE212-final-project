import random
class DiceGame:
    def __init__(self):
        self.dice = []
        self.score = 0
        self.head = None
        self.tail = None
    
    class Die:
        def __init__(self):
            self.number_roll = 0
            self.next = None
            self.prev = None
        
        def get_roll(self):
            """Get a new roll. """
            self.number_roll = random.randint(1, 6)
    
    def start_game(self):
        self.new_roll()
        self.get_user_input()
    
    def new_roll(self):

        # Append new values to the array.
        self.enqueue_dice()

        # Gives nodes new values
        self.roll_dice()

        
        # Display the array.
        self.display_dice()

        # Sort the array.
        self.sort_dice()

        # Dequeue an element on the array.
        self.dequeue_dice()

        # Display the array.
        self.display_dice()

    def enqueue_dice(self):
        """This method is ment to enqueue 6 nodes starting with self.head"""
        node = self.Die()
        self.head = node

        #######################################
        # Challenge 1
        # Add code in this method to enqueue 5
        # nodes to self.head.
        #######################################

    
    def roll_dice(self):
        node = self.head
        i = 1
        while node is not None:
            node.get_roll()
            node = node.next

                
    def sort_dice(self):
        """This method sorts the dice."""
        node = self.head
        #self.display_dice()
        print()
        swapped = True
        while swapped:
            node = self.head
            swapped = False

            while node.next is not None:
                if node.number_roll < node.next.number_roll:
                    # swap stuff
                    switch_prev = node.prev

                    right_node = node.next

                    if switch_prev is not None:
                        node.prev.next = right_node
                    if right_node.next is not None:
                        right_node.next.prev = node

                    node.prev = node.next
                    node.next = right_node.next

                    right_node.next = node
                    right_node.prev = switch_prev

                    swapped = True
                    if node == self.head:
                        self.head = right_node
                else:
                    node = node.next
                


    def display_dice(self):
        """This method displays the dice to the user."""
        node = self.head
        while node is not None:
            print(node.number_roll, ", ", sep="", end="")
            node = node.next
        print()

    def dequeue_dice(self):
        """This method 'picks up' the highest die and displays it.
           It also updates the users score and displays it."""

        # Check if array is empty with the common queue operation empty() 
        if self.head is None:
            print("No dice!")
            self.start_game()
            return

        self.score += self.head.number_roll
        print("You kept", self.head.number_roll, "Your score is:", self.score)

        #######################################
        # Challenge 2
        # Add code in this method to dequeue 1
        # node.
        #######################################

        
    
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