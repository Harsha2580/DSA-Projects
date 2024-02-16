import random
import time
import json

# Constants  
WORD_FILE = "D:\DSA-Projects\Typing Master\words.json" # Modify your Path
LEADERBOARD_FILE = "D:\DSA-Projects\Typing Master\leaderboard.json" # Modify your Path

# Load words from JSON file
def load_words_from_json():
    with open(WORD_FILE, 'r') as file:
        return json.load(file)

# Update and sort leaderboard
def update_leaderboard(player_name, player_wpm):
    leaderboard = load_leaderboard()
    leaderboard.append({"username": player_name, "wpm": player_wpm})
    leaderboard = sorted(leaderboard, key=lambda x: x["wpm"], reverse=True)[:5]
    with open(LEADERBOARD_FILE, 'w') as file:
        json.dump(leaderboard, file)

# Show leaderboard
def show_leaderboard():
    leaderboard = load_leaderboard()
    print("\nLeaderboard:")
    for entry in leaderboard:
        print(f"{entry['username']} - {entry['wpm']} WPM")

# Load leaderboard from JSON file
def load_leaderboard():
    try:
        with open(LEADERBOARD_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Get user input
def get_user_input():
    return input("\nEnter your choice: ")

# Main game logic
def main():
    print("Welcome to Terminal Typing Master!")
    player_name = input("Enter your username: ")

    while True:
        print("\nMenu:")
        print("1. Start Typing Test")
        print("2. Show Leaderboard")
        print("3. Exit")

        choice = get_user_input()

        if choice == '1':
            words = load_words_from_json()
            random.shuffle(words)
            start_time = time.time()

            print("\nType the following words:")
            for word in words:
                print(word, end=' ')
            user_input = input("\n")

            end_time = time.time()
            time_taken = end_time - start_time
            words_typed = len(user_input.split())
            wpm = int((words_typed / time_taken) * 60)

            print(f"\nWords Typed: {words_typed}")
            print(f"Time Taken: {time_taken:.2f} seconds")
            print(f"Words Per Minute (WPM): {wpm}")
            
            update_leaderboard(player_name, wpm)

        elif choice == '2':
            show_leaderboard()

        elif choice == '3':
            print("Exiting. Thank you for playing!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
