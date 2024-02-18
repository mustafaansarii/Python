import random
class RPSGame:
    def __init__(self):
        self.userscore = 0
        self.computerscore = 0
        self.Ties = 0
        self.name = input("Enter Your Name:")

    def play_game(self):
        print(f"{self.name} Welcome! to the Rock Paper Scissors Game\n")
        print("""The winning rules of the game are:
        between rock and paper: Paper wins
        between rock and scissors: Rock wins
        between paper and scissors: Scissors wins\n""")

        while True:
            try:
                print("Choose between the following: \npress 1 for rock \npress 2 for paper \npress 3 for Scissors")
                user_choice = int(input("Enter your choice 1, 2, or 3: "))

                while user_choice > 3 or user_choice < 1:
                    user_choice = int(input("Enter your choice 1, 2, or 3: "))

                if user_choice == 1:
                    uc = "Rock"
                elif user_choice == 2:
                    uc = "Paper"
                else:
                    uc = "Scissors"

                print(self.name, "choose: ", uc)
                print("\nNow computer chooses...")

                computer_choice = random.randint(1, 3)

                if computer_choice == 1:
                    cc = "Rock"
                elif computer_choice == 2:
                    cc = "Paper"
                else:
                    cc = "Scissors"

                print("Computer choose: ", cc)

                if (uc == "Rock" and cc == "Paper") or (uc == "Paper" and cc == "Rock"):
                    print("*****Paper Wins****")
                elif (uc == "Rock" and cc == "Scissors") or (uc == "Scissors" and cc == "Rock"):
                    print("\n****Rock wins****")
                elif uc == cc:
                    print("\nIt's a tie!")
                else:
                    print("\nScissors wins!")

                repeat = input("\nDo you want to play again? (Yes/No): ")
                if repeat.lower() != "yes":
                    break
            except ValueError:
                print("\nInvalid input! Please enter a number (1, 2, or 3).")

        print("Thank you for playing This Game!")


if __name__ == "__main__":
    game = RPSGame()
    game.play_game()
