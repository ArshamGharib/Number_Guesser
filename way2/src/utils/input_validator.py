def validate_user_guess(user_guess):
        if not user_guess.isdigit():
            print('Invalid input!! Please try again.')
            return False
        user_guess = int(user_guess)
        if user_guess > 100 or user_guess < 1 :
            print('Number is out of range, Choose number between 1 to 100!!')
            return False

        return True