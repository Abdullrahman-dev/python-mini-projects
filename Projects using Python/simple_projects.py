import random # import a random class for the game
import string

# Function that cheack if the number is odd or even :
def numberIsOddOrEvene():
    num = int(input('Enter a number to cheack if it\' a \'Odd\' or \'Evene\' : '))
    if num == 0 or num == 1 :
        print('please enter a number bigger than \'0\' or \'1\'')
        numberIsOddOrEvene()
    elif num % 2 == 0 :
        print(f"It\'s a even number : {num}")
    else:
        print(f'It\' a odd number : {num}')

# numberIsOddOrEvene()


# oop in python inside a function that takes a name and age of human and print it: 
def humanObject(name,age):
    class Human :
        def __init__(self,name,age):
            self.name = name 
            self.age = age
        def __str__(self):
            return f"Name: {self.name}, Age: {self.age}"
    print(Human(name,age))

# humanObject("Abdulrahman",21)


# Calculate function : 

def sub(myList): # function to take a list and sub the elements
    total_sub = myList[0]
    for num in myList[1:]:
        total_sub -= num
    return total_sub

def mul(myList): # function to take a list and mul the elements
    total_mul = 1
    for num in myList:
        total_mul *= num
    return total_mul

def div(myList): # function to take a list and div the elements
    total_div = myList[0]
    for num in myList[1:]:
        if num == 0: # check before the user put a 0 input bc will by an error 
            return "Error: Division by zero"
        total_div /= num
    return total_div

def calculate():
    sign = input("Choose operation (+, -, *, /): ")

    print("Enter numbers one by one. Type -1 to stop:")
    myList = []
    while True: # this loop will be forever if dosen't brake by the if condition 
        element = float(input())
        if element == -1: # to brake the while loop,also check the number before put it inside my list 
            break
        myList.append(element)

    if not myList: # if the list is empty
        print("No numbers entered.")
        return

    # check sign the user put it and returen a Result 
    if sign == '+':
        print(f"Result = {sum(myList)}")
    elif sign == '-':
        print(f"Result = {sub(myList)}")
    elif sign == '*':
        print(f"Result = {mul(myList)}")
    elif sign == '/':
        print(f"Result = {div(myList)}")
    else:
        print("Invalid operation.")

# calculate() 


# Game the user traing to guess a random number :

def guessTheNum ():
    print('Try to guess the number, the computer will take a random number between ( 0 and 10 )')
    randomNum = random.randrange(0, 10)
    print('Try to guess the number')
    while True :
        hisGuess = int(input('Enter your guses : '))
        
        lowerGuse = hisGuess - 1 # hint
        uperGuse = hisGuess + 1 #hint
        
        if (randomNum == lowerGuse or randomNum == uperGuse):
            print('Your guess is to close')

        if (hisGuess==randomNum):
            print('Nice you guess the number')
            playAgain = input('If you want to play again type \'Yes\' : ')
            if playAgain.lower == 'yes':
                guessTheNum()
            else:
                break

# guessTheNum()


# Genrating a random password app : 

def randomPassword ():
    length = int(input('Please enter a password length : '))
    lengthSize = 8
    print('''Type the numbers :
          1. Numbers
          2. Character
          3. Special Character
          4. Exit \n ''')
          
    if(lengthSize>length):
        print('Please enter a number bigger or \' 8 \'')
        randomPassword()
    
    characterList = ''
    
    while True :
        userChoses = (input('Enter a number : '))

        if userChoses == '1' :
            characterList += string.digits
        elif userChoses == '2':
            characterList += string.ascii_letters
        elif userChoses == '3':
            characterList += string.punctuation
        elif userChoses == '4':
            break
        else:
            print('Please enter a vaild number')

    password = []

    for i in range(length):
        randomChar = random.choice(characterList)
        password.append(randomChar)

    print('The random password is : ' + ''.join(password))

# randomPassword()