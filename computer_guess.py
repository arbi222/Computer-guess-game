import random

def computer_guess(x):
    low = 1
    high = x
    lives = 7
    feedback = ''
    
    while feedback != 'c' and lives != 0:
        if low != high:
            guess = random.randint(low , high)
        else:
            guess = low # or high cuz high = low 
        
        feedback = input(f"{lives} lives left , Is {guess} too high (H) , too low (L) or correct (C) : ").lower()
        if feedback == 'h':
            high = guess - 1
            lives = lives - 1
        elif feedback == 'l':
            low = guess + 1
            lives = lives - 1
    if lives != 0:
        print(f'Yay !  Computer guessed the number {guess} correctly !!')
    else:
        print(' Computer is out of lives')
computer_guess(100)   