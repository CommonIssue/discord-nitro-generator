

choice = True
import random, string
import os
from termcolor import colored
from colorama import Fore
import requests


print(colored('Nitro Generator -> Menu', 'blue'))
print('')
print(colored('Currently updated! Version: 1 (BETA)', 'blue'))
print('')
print('[1] Generator')
print('[2] Generator + Checker')
print("[3] Exit")
print("")
print("")

choice = input("Choice: ")

if choice == '1':
 print(colored('Nitro Generator v1 -> Generate', 'blue'))
 print(colored('Remember you will have a 1 percent of it working!', 'red'))
 print('')
 print('')


 amount = int(input('Amount: '))
 value = 1
 while value <= amount:
  code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=15))
  f = open('generated.txt', "a+")
  f.write(f'{code}\n')
  print(colored(f'{code}', 'yellow'))
  value += 1
 print("")
 print("")
 input(colored("Finished! Saved to (generated.txt).", 'green'))
 input(colored("Press Enter to exit", 'red'))

elif choice == '2':

 print('')
 print('')
 print(colored('Nitro Generator v1 -> Generate + Checker'))
 print('')
 print('')
 print(colored('If it checks slowly, you are being ratelimited (or bad connection)', 'red'))
 print('')
 print('')
 num = int(input('Amount: '))


 with open("checked.txt", "w", encoding='utf-8') as file:

    print('')
    
    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 15
        ))

        file.write(f"https://discord.gift/{code}\n")


 with open("checked.txt") as file:
    for line in file.readlines():
        code = line.strip("\n")

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(Fore.GREEN + f"\n\nValid | {code}\n")
        else:
            print(Fore.RED + f"Invalid | {code}")

 print('')
 input(Fore.GREEN + 'Saved in checked.txt, press enter to exit the program. ')

elif choice == '3':
 quit()

else:
 print('')
 print('')
 print(colored('Nitro Generator v1 -> Wrong option!', 'blue'))
 print('')
 print("")
 print("")
 print(colored("Incorrect option!", 'red'))
 print("")
 print("")
 input(colored("Press enter to exit the program ", 'yellow'))
