import random
import string

def generate_password(length):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    
    # Combine all characters
    all_chars = lowercase + uppercase + digits + special_chars
    
    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    # Get password length from user
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Generate and display password
    password = generate_password(length)
    print(f"\nYour generated password is: {password}")

if __name__ == "__main__":
    main()
