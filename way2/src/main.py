from src.game_logic.input_validator import validate_user_guess
from src.game_logic.number_generator import generate_random_number
from src.game_logic.hint_generator import hint

def main():
    score = 100
    actual_number = generate_random_number(1, 100)

    while True:
        user_input = validate_user_guess("Enter your guess: ", 1, 100)
        if user_input == actual_number:
            print('Your guess is correct!')
            print(f'Your score is {score}')
            break
        else:
            hint(user_input, actual_number)
            score -= 10
            score = max(0, score)

if __name__ == '__main__':
    main()