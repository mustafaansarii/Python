import random
class GussingGame:
    randNumber = random.randint(1, 100)
    userguess = None
    guesses = 0
    def __init__(self):
        randNumber = random.randint(1, 100)
        userguess = None
        guesses = 0
        while userguess != randNumber:
            userguess = int(input("Enter your guess: "))
            guesses += 1
            if userguess == randNumber:
                print("You Have Guessed right!")
            else:
                if userguess > randNumber:
                    print("You have guessed wrong! Enter smaller number")
                else:
                    print("You have guessed wrong! Enter larger number")
        print(f"You have guessed in {guesses} guesses")
        try:
            with open("Hiscore.txt", "r") as f:
                hiscore = int(f.read())
        except FileNotFoundError:
            hiscore = float('inf')

        if guesses < hiscore:
            print("You have broken the high score")
            with open("Hiscore.txt", "w") as f:
                f.write(str(guesses))

obj=GussingGame()
