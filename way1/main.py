import random
rand_num = random.randint(1, 100)

def validate_user_guess(user_guess):
        if not user_guess.isdigit():
            print('Invalid input!! Please try again.')
            return False
        user_guess = int(user_guess)
        if user_guess > 100 or user_guess < 1 :
            print('Number is out of range, Choose number between 1 to 100! Also, you get 5 negetive points!')
            return False

        return True

score = 100

while True:

    user_guess = input('Guess a number between 1 and 100: ')
    if user_guess == 'q':
        print('Thank you for playing. Goodbye!')
        break
    if not validate_user_guess(user_guess):
        score -= 5
        continue
    user_guess = int(user_guess)
    if user_guess > rand_num:
        print('Number is less than that.')

    elif user_guess == rand_num:
        print(f'Cogratulations! You are correct.')
        print(f'Your score is {score}. See you later:)')
        break
    else:
        print('Number is grater than that.')
    
    score -= 10
    score = max(score, 0)