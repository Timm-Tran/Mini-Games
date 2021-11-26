import random
import getpass
import time

def main():
    choice = int(input('\n\nWelcome to the guessing game! \n\nWould you like to guess (1) \nor for the computer to guess (2)? '))
    if choice == 1:
        playerGuess()
    elif choice == 2:
        computerGuess()
    else:
        print("Eh you're not the brightest are you...")

def playerGuess(low=0, high=100):
    number = random.randint(low, high)
    guess = None
    while guess != number:
        guess = int(input(f"\nGuess an random number between {low} and {high}: "))
        if guess > number:
            print(f'{guess} was too high! Try lower..')
            
        elif guess < number:
            print(f'{guess} was too low! Try higher..')
            
        else:
            print(f'\nYou guessed correctly good job! It was {number}!')


def computerGuess():
    rangelow = int(input(f'What is the lowest guess possible? '))
    rangehigh = int(input(f'What in the highest guess possible? '))
    number = int(getpass.getpass(f'Give me a number to guess, I wont look I promise! '))
    cpuGuess = None
    
    while cpuGuess != number:
        cpuGuess = random.randint(rangelow, rangehigh)
        print(f'\nI guess... {cpuGuess}!')
        time.sleep(3)
        if cpuGuess > number:
            print(f'Shoot, I was too high... Gotta try again!')
            rangehigh = cpuGuess - 1
            time.sleep(2)
            
        elif cpuGuess < number:
            print(f'Shoot, I was too low... Gotta try again!')
            rangelow = cpuGuess + 1
            time.sleep(2)
            
        else:
            print(f"Hey I got it! I'm hella smart get rekt gg ez no re")
            

main()