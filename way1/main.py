import random
rand_num = random.randint(1, 100)

while True:
    user_guess = input('Guess a number between 1 and 100: ')
    if user_guess == 'q':
        print('Thank you for playing. Goodbye!')
        break
    elif not user_guess.isdigit():
        print('Invalid input!! Please try again.')
        continue

    user_guess = int(user_guess)
    if user_guess > 100 or user_guess < 1 :
        print('Number is out of range, Choose number between 1 to 100!')
        continue

    if user_guess < rand_num:
        print('Number is less than that.')
    elif user_guess == rand_num:
        print('Cogratulations! You are correct. See you later:)')
        break
    else:
        print('Number is grater than that.')