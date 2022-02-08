# A Wordle solver

# Variables
guessCount = 0                          # keep track of guess count
nextGuess = "TEARS"                     # Word to guess next
lettersIn = {}                          # letters that are in the word
wordIs = ['','','','','']               # Correct order of letters in word
isNot = {0:[], 1:[], 2:[], 3:[], 4:[]}  # letters that are not in this spot in order
NotIn = {}                              # letters that aren't in the word at all
result = ""                             # Result from entering guess in Wordle

# Intro message
print("Welcome to the WORDLE Solver. Please follow the instructions.\n")

# Open word bank txt file
file = open('WordBank', 'r')

# Create the word bank
WordBank = file.read().splitlines()

# While we still have less than 6 guesses
while guessCount < 7:
    # If we are on first guess, give the intro word "TEARS", else, next best guess
    print("\nTry this word: " + nextGuess);

    # Get the result from WORDLE of our guess
    while True:
        # get the result from wordle
        result = input("Please enter the result in the form \"GBYGG\".\n").upper()

        # Length is 5, else reprompt
        if len(result) == 5:
            break
        else:
            print("Please enter 5 characters.\n")

    # If answer is correct, win message
    if result == "GGGGG":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("Congratulations! You cheated to win! Goodbye!\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        break

    # Fill in the information structures
    for i, letter in enumerate(result):
        # If green, fill in LettersIn and WordIs
        if letter == 'G':
            lettersIn[nextGuess[i]] = 1
            wordIs[i] = nextGuess[i]
        # If yellow, fill in letters in and isNot
        elif letter == 'Y':
            lettersIn[nextGuess[i]] = 1
            isNot[i].append(nextGuess[i])
        # If black, just add to not in
        else:
            NotIn[nextGuess[i]] = 1

    # Filter word bank down

    saveFlag = 0
    index = 0

    # While not at end of file
    while index < len(WordBank):

        # set flag to 0
        indexFlag = 0

        # Reset length of numArr
        #lenOfNumArr = len(lettersIn.keys())
        lettersInCopy = list(lettersIn.keys())

        # For each letter in the current word in the word bank
        for i, letter in enumerate(WordBank[index]):
            letter = letter.upper()
            # If there's no chance its this word by length OR
            # if the letter is in the NOT IN dict OR the definitely not at this spot dict OR
            # than pop and go next
            if len(lettersInCopy) + i > 5 or letter in NotIn.keys() or letter in isNot[i]:
                WordBank.pop(index)
                indexFlag = 1
                break

            # if the letter doesn't match with the WordIs correct dict
            if wordIs[i] != '' and letter != wordIs[i]:
                WordBank.pop(index)
                indexFlag = 1
                break

            # Pop from the copy list if we see a letter that's in the word
            if letter in lettersInCopy:
                lettersInCopy.remove(letter)

            # If we're on last one, and there's last char doesn't match, pop
            if i == 4 and len(lettersInCopy) != 0:
                WordBank.pop(index)
                indexFlag = 1
                break

        # Iterate to next item
        if indexFlag == 0:
            # Save the guess
            if saveFlag == 0:
                nextGuess = WordBank[index].upper()
                saveFlag = 1

            # Go to next element in word bank
            index += 1

    # Increment the guess count
    guessCount += 1