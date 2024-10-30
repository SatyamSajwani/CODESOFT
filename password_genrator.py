import random  # Import the random module to pick random characters
import string  # Import string module to get letters, digits, and symbols

# Ask the user for the desired password length
length = int(input("Enter the desired length for the password: "))

# Define the characters that can be used in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate a random password by choosing random characters
password = ""
for i in range(length):
    password += random.choice(characters)  # Add a random character to the password

# Display the generated password
print("Generated Password:", password)
