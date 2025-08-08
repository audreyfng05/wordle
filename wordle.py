"""A program that mimics Wordle in which the player has to guess the secret word."""

__author__: str = "730756822"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # Turn starts at 1
    turn = 1
    # Game runs up to <=6 turns
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        # Player enters guess word, which is the same length as the secret word
        guess = input_guess(guess_length=len(secret))
        # Emoji string based on the player's guess word
        emoji_string = emojified(guess=guess, secret=secret)
        print(emoji_string)
        # Prints if the guess matches the secret word
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            return
        # Goes to the next turn if not word not guessed correctly
        else:
            turn += 1
    # If the player uses all 6 turns without guessing the secret word
    print("X/6 - Sorry, try again tomorrow!")


def contains_char(search: str, char: str) -> bool:
    """Checks if the character (char) is in the string (search)."""
    assert len(char) == 1, f"len('{char}') is not 1"
    # Starts the index at 0 to search starting from
    # the first character in the search string
    idx: int = 0
    # Loops through each character index in the string
    while idx < len(search):
        # Checks if the current character matches the inputted character
        if search[idx] == char:
            return True
        # Ensures that the loop moves to the next character index
        idx += 1
    return False


WHITE_BOX: str = "\U00002b1c"
GREEN_BOX: str = "\U0001f7e9"
YELLOW_BOX: str = "\U0001f7e8"


def emojified(guess: str, secret: str) -> str:
    """Returns an emoji string whose color codifies the
    results of a guess using Wordle's logic.
    The string guess is the player's guess word and the
    secret guess is the secret word the player is trying to guess.
    """
    assert len(guess) == len(secret), "Guess must be same length as secret"
    # Starts the index at 0 to search starting
    # from the first character in the guess string
    idx: int = 0
    # Adds the string of emojis starting from
    #  this result string, which is an empty string
    result: str = ""
    while idx < len(guess):
        # If character position in guess word matches character
        #  position in secret word, use green box emoji
        if guess[idx] == secret[idx]:
            result += GREEN_BOX
        else:
            # If character in guess word is in secret word, use yellow box emoji
            if contains_char(search=secret, char=guess[idx]):
                result += YELLOW_BOX
            # Otherwise, the character in guess word is not in
            # the secret word, so use the white box emoji
            else:
                result += WHITE_BOX
        idx += 1
    return result


def input_guess(guess_length: int) -> str:
    """Prompts the player for a guess and continues
    until they provide a guess of the expected length (guess_length)."""
    # Prompts the player to enter a word of the expected length
    guess: str = input(f"Enter a {guess_length} character word: ")
    # If the guess word matches the expected length, returns the word
    if guess_length == len(guess):
        return guess
    else:
        # Prompts the player to keep entering a word with the expected length
        while guess_length != len(guess):
            print(f"That wasn't {guess_length} chars! Try again: ")
            guess = input(f"Enter a {guess_length} character word: ")
    # Returns the guess
    return guess


if __name__ == "__main__":
    main(secret="codes")