import random
import string

def generate_username(include_numbers=True, include_special_chars=False, length=8):
    adjectives = ["Cool", "Fast", "Happy", "Clever", "Brave", "Witty", "Lucky", "Chill"]
    nouns = ["Tiger", "Panda", "Dragon", "Falcon", "Eagle", "Wolf", "Shark", "Phoenix"]
    
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun
    
    if include_numbers:
        username += str(random.randint(10, 99))
    
    if include_special_chars:
        special_chars = "@#$%&*!"
        username += random.choice(special_chars)
    
    return username[:length]

def save_to_file(username, filename="usernames.txt"):
    with open(filename, "a") as file:
        file.write(username + "\n")
    print(f"Username saved to {filename}")

def main():
    print("Welcome to the Random Username Generator!")
    
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
    length = int(input("Enter username length (default 8): ") or 8)
    
    username = generate_username(include_numbers, include_special_chars, length)
    print("Generated Username:", username)
    
    save_choice = input("Do you want to save this username? (y/n): ").strip().lower()
    if save_choice == 'y':
        save_to_file(username)
    
if __name__ == "__main__":
    main()