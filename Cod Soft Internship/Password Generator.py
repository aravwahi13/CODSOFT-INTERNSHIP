import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for a secure password.")
        return

    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of the password: "))

        # Generate the password
        password = generate_password(length)

        if password:
            print(f"Generated Password: {password}")

    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
