import random 
# Number guessing game
# beginner friendly project for Github

while True:

 print(' \nWelcome To Number Guessing Game\n ')

# Ask user to choose difficulty 
 print('1. Easy (lives 15)') 
 print('2. Normal (lives 10)')
 print('3. Hard (lives 5)')

 choice = int(input('Enter your choice which level you want (1/2/3):'))

#Set lives based on difficulty
 if choice == 1:
   lives = 15

 elif choice == 2:
   lives = 10

 elif choice == 3:
   lives = 5

 else :
   print('Invalid Text')
   continue
#Generate a random number 1 to 100
 computer = random.randint(1,100)
 attempts = 0

#Main guessing loop
 while lives > 0:

   attempts += 1

   user_guess = int(input("Guess the number 1 to 100:"))

   if computer == user_guess:
    print(f'You Win  |remaining lives {lives}|')
    break

   elif computer > user_guess:
    lives -= 1
    print(f'Too Low  |remaining lives {lives}|')

   else:
    lives -= 1
    print(f'Too High  |remaining lives {lives}| ')    
 
#Game over message
 if lives == 0:
    print('GAME OVER')
    print('Computer number was',computer)
    
 print(f'You guessed it in {attempts} tries')
#Ask if player wants to play again
 answer = input('Do you want to play again (yes/no)').lower()

 if answer == 'no':
  print('Thankyou for playing')
  break








