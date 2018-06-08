import random

HANGMANPICS = ['''

    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
         
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
        
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
        
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
        
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''
        
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']

WORDS = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def randomWord():
    word = WORDS[random.randint(0, len(WORDS)-1)]
    return word

def displayGame(word, missedLetters, correctLetters, hangman=HANGMANPICS):
    print("\nHANGMAN\n")
    
    print("Missed Letters: " + " ".join(missedLetters))
    wrongNum = len(missedLetters)
    print(HANGMANPICS[wrongNum])

    wordDisplay = ""
    correctIndex = [i for i, x in enumerate(word) if x in correctLetters]
    for i in range(len(word)):
        if i in correctIndex:
            wordDisplay += word[i] + " "
        else:
            wordDisplay += "_" + " "
    print("\n" + wordDisplay)
    return correctIndex

def guessLetter(missedLetters, correctLetters, correctCount):
    guess = input("Guess a letter: ")
    if guess in word:
        correctLetters.append(guess)
        correctCount += word.count(guess)
    else:
        missedLetters.append(guess)
    return correctCount

def gameStatus(word, correctCount, missedLetters):
    if len(missedLetters) >= 6:
        return "lost"
    elif correctCount == len(word):
        return "won"
    else:
        return "continue"

def playAgain():
    play = input("Play again? ")
    if play.lower() == "y":
        return True
    return False

if __name__ == "__main__":
    play = True
    while play == True:
        word = randomWord()
        correct = []
        incorrect = []
        correctCount = 0;
        status = gameStatus(word, correctCount, incorrect)
        while status == "continue":
            correctIndex = displayGame(word, incorrect, correct)
            correctCount = guessLetter(incorrect, correct, correctCount)
            status = gameStatus(word, correctCount, incorrect)
        if status == "won":
            print("Congratulations! You won!")
        elif status == "lost":
            print("Oh no! Looks like you lost!")
        play = playAgain()


        
               
