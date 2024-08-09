import random

def high_low_game():
    # Step 1: Generate a random 4-digit number
    target_number = random.randint(1000, 9999)
    
    print("Welcome to the High-Low Game!")
    print("I have selected a 4-digit number. Try to guess it!")

    # Step 2: Loop until the user guesses correctly
    while True:
        # Step 3: Get the user's guess
        guess = int(input("Enter your 4-digit guess: "))
        
        # Step 4: Compare the guess to the target number
        if guess < target_number:
            print("Too Low!")
        elif guess > target_number:
            print("Too High!")
        else:
            # Step 5: Correct guess, break the loop
            print(f"Congratulations! You guessed the correct number: {target_number}")
            break

if __name__ == "__main__":
    high_low_game()
