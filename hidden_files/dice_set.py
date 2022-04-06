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
        my_set = set()
        for die in self.dice:
            if die in my_set:
                self.score += 1
            my_set.add(die)
        

game = DiceGame()
game.start_game()