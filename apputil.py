# Q1
import string


def palindrome(word):
    """Return True if word is a palindrome, ignoring case, spaces, and punctuation."""
    word = word.lower()

    cleaned = ""
    for char in word:
        if char not in string.punctuation and char != " ":
            cleaned += char

    return cleaned == cleaned[::-1]


# Q2
def parentheses(sequence):
    """Return True if parentheses in the sequence are balanced."""
    count = 0

    for char in sequence:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1

        if count < 0:
            return False

    return count == 0


if __name__ == "__main__":
    print(palindrome("racecar"))                    # True
    print(palindrome("Nurses Run"))                 # True
    print(palindrome("Sit on a potato pan, Otis.")) # True
    print(palindrome("Hello world"))                # False

    print(parentheses("((blah)()()())"))            # True
    print(parentheses("(((())blee))"))              # True
    print(parentheses("(()hello((())()))"))         # True
    print(parentheses("((((((())"))                 # False
    print(parentheses("()))"))                      # False
