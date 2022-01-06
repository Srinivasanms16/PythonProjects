import random as rd 
from colorama import Fore, Back, Style, init

#this to inilize the colorama 
init()

lowerlimit = input("lower limit :")
higherlimit = input("higher limit :")

#userGuess
def guess(lowerlimit,higherlimit):
    result = rd.randint(int(lowerlimit),int(higherlimit))
    guess = int(input("Guess the number :"))
    while(True):
        if(guess > result):
            print(Fore.RED + "Guess is greater")
            guess = int(input("Guess the number :"))
        elif(guess < result):
            print(Fore.RED + "Guess is lesser")
            guess = int(input("Guess the number :"))
        else:
            print(Fore.GREEN + f"you guessed correct value {result}")
            break

#computer guess
def computerguess(lowerlimit,higherlimit):
    print(Fore.GREEN + "if computer guess is lower(L),higher(H),correct(C)")
    result = rd.randint(int(lowerlimit), int(higherlimit))
    while(True):
        print(Fore.RED + f"number is {result}")
        feedback = input("feedback :").lower()
        if(feedback == "l"):
            lowerlimit = int(result) + 1
            result = rd.randint(int(lowerlimit), int(higherlimit))
        elif(feedback == "h"):
            higherlimit = int(result) - 1
            result = rd.randint(int(lowerlimit), int(higherlimit))
        else:
            print(Fore.GREEN + f"Computer guessed correctly vaule is {result}")
            break


guess(lowerlimit,higherlimit)