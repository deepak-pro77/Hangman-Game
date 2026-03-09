import random


class HangmanGame:

    def __init__(self):
        self.words = ["python", "programming", "computer", "table", "coding"]
        self.word = random.choice(self.words)
        self.guessed_letters = []
        self.attempts_left = 6

    def display_word(self):

        display = ""

        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display)

    def guess_letter(self):

        guess = input("\nGuess the letter: ").lower()

        if guess in self.guessed_letters:
            print("You already guessed that letter")
            return

        self.guessed_letters.append(guess)

        if guess not in self.word:
            self.attempts_left -= 1
            print("❌ Wrong Guess")
        else:
            print("✅ Correct Guess")

    def check_win(self):

        for letter in self.word:
            if letter not in self.guessed_letters:
                return False

        return True

    def start_game(self):

        print("\n HANGMAN GAME")
        print("-" * 30)

        hangman_stages = [
            """


""",
            """
  O
""",
            """
  O
  |
""",
            """
  O
 /|
""",
            """
  O
 /|\\
""",
            """
  O
 /|\\
 /
""",
            """
  O
 /|\\
 / \\
"""
        ]

        while self.attempts_left > 0:

            self.display_word()
            print("Attempts Left:", self.attempts_left)
            print("Guessed Letters:", self.guessed_letters)

            self.guess_letter()

            print(hangman_stages[6 - self.attempts_left])

            if self.check_win():
                print("Congratulations! You won the game")
                return

        print("GAME OVER")
        print("The Correct Word was:", self.word)


game = HangmanGame()

if __name__ == "__main__":
    game.start_game()
