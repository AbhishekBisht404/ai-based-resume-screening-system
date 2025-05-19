import random

def show_menu():
    print("\n=== Number Guessing Game ===")
    print("Choose difficulty level:")
    print("1. Easy (1–10)")
    print("2. Medium (1–50)")
    print("3. Hard (1–100)")
    print("4. Exit")

def get_range(level):
    if level == '1':
        return 1, 10
    elif level == '2':
        return 1, 50
    elif level == '3':
        return 1, 100
    else:
        return None, None

def play_game(min_val, max_val):
    secret = random.randint(min_val, max_val)
    attempts = 0
    print(f"\nGuess the number between {min_val} and {max_val}!")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess < min_val or guess > max_val:
                print("Out of range. Try again.")
            elif guess < secret:
                print("Too low.")
            elif guess > secret:
                print("Too high.")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice in ['1', '2', '3']:
            min_val, max_val = get_range(choice)
            play_game(min_val, max_val)
        elif choice == '4':
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
