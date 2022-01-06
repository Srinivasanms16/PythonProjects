import random as rd 
from colorama import Fore, Back, Style,init

#this to inilize the colorama 
init()

def rock_papper_Sicc():
    print(Fore.MAGENTA + "Rock(r) Papper(p) Scissors(s)")
    user = input("your Choice :").lower()
    comp = rd.choice(['r','p','s'])
    print(Fore.YELLOW + f"computer selected {comp}")
    if(user == comp):
        print(Fore.CYAN + "its tie")
    elif((user == 'r' and comp == 'p') or (user == 'r' and comp == 's') or (user == 's' and comp == 'p')):
        print(Fore.GREEN + "user wins")
    else:
        print(Fore.RED + "computer wins")

rock_papper_Sicc()