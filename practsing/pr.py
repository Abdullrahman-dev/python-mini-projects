# Another game qustions :

def qustions_game () :
    
    qustions = (
        "1. Who developed Python Programming Language?",
        "2. Which type of Programming does Python support?",
        "3. Is Python case sensitive when dealing with identifiers?",
        "4. Which of the following is the correct extension of the Python file?",
        "5. Is Python code compiled or interpreted?"
    )

    # answers
    answers = ((
        "a) Wick van Rossum",
        "b) Rasmus Lerdorf",
        "c) Guido van Rossum",
        "d) Niene Stom"
    ),
    (
        "a) object-oriented programming",
        "b) structured programming",
        "c) functional programming",
        "d) all of the mentioned"
    ),
    (
        "a) no",
        "b) yes",
        "c) machine dependent",
        "d) none of the mentioned"
    ),
    (
        "a) .python",
        "b) .pl",
        "c) .py",
        "d) .p"
    ),
    (
        "a) Python code is both compiled and interpreted",
        "b) Python code is neither compiled nor interpreted",
        "c) Python code is only compiled",
        "d) Python code is only interpreted"
    ))

    real_answer = ["c","d","b","c","a"]

    qustion_num = 0
    guesses = []
    score = 0 

    for qustion in qustions:
        qustion_number = 1
        print(f"----- Qustion Number \'{qustion_number}\' -----")
        print(qustion)
        
        for answer in answers[qustion_num]:
            print(answer,end="\n")


        guess = str(input("Enter a Latter of your answer : "))
        guesses.append(guess)        

        if guess == real_answer[qustion_num]:
            print("CORRECT !")
            score += 1
        else:
            print("WRONG !")

        qustion_num += 1

    print(f"Your score is : \'{score}\'")

    print("--- --- --- --- ---")
    print("Real Answers is : ")
    for i in real_answer :
        print(f"({i})", end=" ")
    print("")
    print(f"Your Answers is : ")
    for i in guesses :
        print(f"({i})",end=" ")

qustions_game ()


# Guess the name game : 

import random 

def guess_name ():
    
    words = ["python","Web programing","Laravel","PHP","Front end","Back end"]
    word = random.choice(words)
    word = word.lower()
    guessed = ["_"for _ in word]
    attemps = 6
    print_once = False
    round = 1

    while attemps > 0 and "_" in guessed :
        print(f"\n------- Guess {round} -------\n")
        round += 1
        print("Word :","".join(guessed))
        
        if not print_once:
            print(f"The length of the word is : {len(word)}")
            print_once = True

        guess = input("Guess a letter (\'Type the letter in lower case\'): ")

        if guess in word :
            for i in range(len(word)):
                if word[i] == guess :
                    guessed[i] = guess
                    print("Your guess correct")
                    if "_" not in guessed :
                        print(word)
        else:
            attemps -= 1
            print(f"Incorrect attemps left : {attemps}")
        
    if "_" not in guessed :
        print(f"You win, the final word is : {word}")
    elif attemps == 0 :
        print(f"You lose< the final word is : {word}")

# guess_name()


# Word Scramble :

def scramble_word(word):
   return "".join(random.sample(word, len(word)))

def word_scramble ():

    words = ["python","Web programing","Laravel","PHP","Front end","Back end"]
    correct_word = random.choice(words)
    word = scramble_word(correct_word)
    attemps = 6

    while attemps > 0 :
        
        print(f"Guess the word : \'{word}\'")
        guess = input("Enter your guess : ")

        if guess.lower == correct_word.lower :
            print(f"You win and the word is : \'{correct_word}\'")
            break
        else:
            attemps -= 1
            print(f"Incoorect, Your remaing attemps is : \'{attemps}\'")
    
    if attemps == 0 :
        print(f"You loast and the word is : \'{correct_word}\'")

# word_scramble()

