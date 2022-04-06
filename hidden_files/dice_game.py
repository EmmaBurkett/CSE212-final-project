import random
class DiceGame:
    def __init__(self):
        self.dice = []
        self.score = 0
    
    def start_game(self):
        self.new_roll()
        self.get_user_input()
    
    def new_roll(self):
        self.get_dice()
        self.sort_dice()
        self.display_dice()
        self.dequeue_dice()
        self.display_dice()

    def get_dice(self):
        """This function 'rolls' the dice."""

        # Enqueue a value to an array:
        for i in range(6):
            self.dice.append(random.randint(1,6))
    
    def sort_dice(self):
        """This function sorts the dice."""

        for i in range(6):
            for j in range(i, 6):
                if self.dice[i] < self.dice[j]:
                    switch = self.dice[i]
                    self.dice[i] = self.dice[j]
                    self.dice[j] = switch

    def display_dice(self):
        """This function displays the dice to the user."""

        print(*self.dice, sep=", ")

    def dequeue_dice(self):
        """This function 'picks up' the highest die and displays it.
           It also updates the users score and displays it."""

        # Check if array is empty with the common queue operation empty() 
        if len(self.dice) == 0:
            print("No dice!")
            return

        # Dequeue() the first die in the array and display to the user.
        first_die = self.dice.pop(0)

        self.score += first_die
        print("You kept", first_die, "Your score is:", self.score)
    
    def get_user_input(self):
        """"This function asks the user if they would like to 'pick up'
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