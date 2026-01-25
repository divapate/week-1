#Q1
import string

def palindrome(word):
    # Convert to lowercase
    word = word.lower()
    
    # Remove spaces and punctuation
    cleaned = ""
    for char in word:
        if char not in string.punctuation and char != " ":
            cleaned += char
    
    # Check if the cleaned word is the same forwards and backwards
    return cleaned == cleaned[::-1]
import string

print(palindrome("racecar"))                    # True
print(palindrome("Nurses Run"))                 # True
print(palindrome("Sit on a potato pan, Otis.")) # True
print(palindrome("Hello world"))                # False


#Q2
def parentheses(sequence):
    count = 0 # always initialize 

    for char in sequence:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1

        # If we close more than we open
        if count < 0:
            return False

    # Is the count zero though? if not return false handels count > 1 error 
    return count == 0
print(parentheses("((blah)()()())"))     # True
print(parentheses("(((())blee))"))       # True
print(parentheses("(()hello((())()))"))  # True
print(parentheses("((((((())"))          # False
print(parentheses("()))"))               # False

