# 1 Importing statement

from spellchecker import SpellChecker

# 2 Initialising the spellchecker

spell = SpellChecker()

# 3 Getting the input from the user

word = input("inter the miss spell word: ")

# 4 Checking the spelling 

corrected_word = spell.correction(word)

# 5 Displaying the corrected word

print(corrected_word)