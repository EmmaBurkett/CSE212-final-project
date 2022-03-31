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
        
        # Enqueue values in a linked list.

        # Enqueue a value to an array:
        if self.head is None:
            self.head = self.Die()
            self.head.get_roll()
            self.head.next = self.Die()
            self.head.next.prev = self.head
        
        for i in range()

    
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