
from colorama import Fore, Back, Style,init

#this to inilize the colorama 
init()

name = input("name :")
age = input("age :")
place = input("place :")

madlib = f"Hello {name}, your age is {age}. Welcome to {place}"

print(Style.BRIGHT + Fore.GREEN  + madlib +"\n")
print(Back.RED + Fore.WHITE + madlib)
