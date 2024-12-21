import secrets
import string

def generate_password(length=12):
    """
    Generate a secure password using a mix of characters.
    Modern password requirements:
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    - Minimum length of 12 characters
    """
    if length < 12:
        raise ValueError("Password length must be at least 12 characters.")
    
    # Character sets
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation
    all_characters = letters + digits + special_characters

    # Ensure the password meets modern security requirements
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(digits),
        secrets.choice(special_characters)
    ]

    # Fill the rest of the password length
    password += [secrets.choice(all_characters) for _ in range(length - 4)]

    # Shuffle the result to avoid predictable patterns
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

# Display user details before execution
print("Name: Talha Ahmed")
print("Registration Number: F2020065084")

# Generate the password
try:
    secure_password = generate_password()
    print("\nGenerated Secure Password: ", secure_password)
except ValueError as e:
    print(e)

# Display user details after execution
print("\nName: Talha Ahmed")
print("Registration Number: F2020065084\n")
