import os
# Validating user's login credentials
# Predefined credentials (for demonstration purposes)
credentials = {
    "David": "password123",
    "John": "securepass",
    "Tom": "mypassword"
}

# Function to validate login credentials
def validate_login(username, password):
    if username not in credentials:
        print("Invalid username")
    elif credentials[username] != password:
        print("Invalid password")
    else:
        print("Login successful")

# Example usage
username = input("Enter your username: ")
password = input("Enter your password: ")
validate_login(username, password)
