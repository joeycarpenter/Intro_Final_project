import time
import random

def generate_random_sentence(difficulty):
    easy_sentences = [
        "The cat sat on the mat.",
        "The sky is blue.",
        "We are penn state.",
        "I love music.",
        "kendrick better."
    ]
    medium_sentences = [
        "The steelers are going to win the super bowl.",
        "The quick brown fox jumps over the lazy dog.",
        "To be or not to be, that is the question.",
        "A journey of a thousand miles begins with a single step.",
        "The things that we own end up owning us."
    ]
    hard_sentences = [
        "Joey is the greatest coder in the world.",
        "It's not about the years in our life, it's about the life in our years.",
        "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.",
        "How much can you know about yourself if you have never been in a fight?",
        "It's not about the destination, it's about the journey."
    ]
    if difficulty == 'easy':
        return random.choice(easy_sentences)
    elif difficulty == 'medium':
        return random.choice(medium_sentences)
    else:  # hard
        return random.choice(hard_sentences)

def calculate_accuracy_and_errors(user_input, text):
    min_length = min(len(text), len(user_input))
    correct_chars = sum(1 for u, t in zip(user_input[:min_length], text[:min_length]) if u.lower() == t.lower())
    accuracy = correct_chars / len(text) * 100

    errors = {
        "substitutions": [],
        "omissions": [],
        "additions": []
    }

    for i, (u, t) in enumerate(zip(user_input, text)):
        if u.lower() != t.lower():
            errors["substitutions"].append((i, t, u))

    if len(user_input) < len(text):
        for i in range(len(user_input), len(text)):
            errors["omissions"].append((i, text[i]))

    if len(user_input) > len(text):
        for i in range(len(text), len(user_input)):
            errors["additions"].append((i, user_input[i]))

    return accuracy, errors

def display_results(elapsed_time, accuracy, text, user_input, errors):
    print(f"\nTime taken: {elapsed_time:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Your typing speed: {len(text) / (5 * elapsed_time):.2f} words per minute")
    print(f"Keystrokes per minute: {len(user_input) / (elapsed_time / 60):.2f}")

    if accuracy >= 90:
        print("You're a typing master!")
    elif 80 <= accuracy < 90:
        print("Good job! Let's aim for perfection.")
    elif 70 <= accuracy < 80:
        print("Above average, but could use improvement. Remember, practice makes perfect!")
    else:
        print("Keep practicing! You'll improve with time.")

    if user_input != text:
        print("\nDetailed Error Analysis:")

        if errors["substitutions"]:
            print("Substitutions:")
            for position, correct, typed in errors["substitutions"]:
                print(f"Position {position + 1}: Correct letter: '{correct}', what you typed: '{typed}'")

        if errors["omissions"]:
            print("Omissions:")
            for position, correct in errors["omissions"]:
                print(f"Position {position + 1}: Omitted letter: '{correct}'")

        if errors["additions"]:
            print("Additions:")
            for position, typed in errors["additions"]:
                print(f"Position {position + 1}: Added letter: '{typed}'")

def typing_test():
    print("Welcome to the Typing Speed Test by Joey Carpenter!")
    print("This test will help you measure your typing speed and accuracy.")
    print("You can choose from three difficulty levels: easy, medium, and hard.")
    print("You will be given a sentence to type as quickly and accurately as possible.")
    print("Your performance will be evaluated based on your typing speed (words per minute) and accuracy.")
    print("Let's get started!\n")

    difficulty = input("Choose a difficulty level (easy, medium, hard): ").strip().lower()
    while difficulty not in ['easy', 'medium', 'hard']:
        difficulty = input("Invalid choice. Please choose a difficulty level (easy, medium, hard): ").strip().lower()

    text = generate_random_sentence(difficulty)
    print("\nType the following sentence:")
    print(f"\n{text}\n")
    input("Press Enter when you're ready to start...")

    start_time = time.time()
    user_input = input("Type the text here: ")
    end_time = time.time()
    elapsed_time = end_time - start_time

    accuracy, errors = calculate_accuracy_and_errors(user_input, text)
    display_results(elapsed_time, accuracy, text, user_input, errors)

    play_again = input("Would you like to play again? (yes/no): ").strip().lower()
    while play_again not in ['yes', 'no']:
        play_again = input("Please enter 'yes' or 'no': ").strip().lower()

    if play_again == "yes":
        typing_test()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    typing_test()



