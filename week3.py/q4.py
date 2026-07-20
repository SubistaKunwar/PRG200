# Question 4 – Password Strength Checker

passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]

special_characters = "!@#$%^&*"

# Loop through each password
for password in passwords:

    print("\nChecking Password:", password)

    # Variables to check each requirement
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    # Check every character in the password
    for character in password:

        if character.isupper():
            has_uppercase = True

        if character.islower():
            has_lowercase = True

        if character.isdigit():
            has_digit = True

        if character in special_characters:
            has_special = True

    # Check whether the password is strong
    if (len(password) >= 8 and
        has_uppercase and
        has_lowercase and
        has_digit and
        has_special):

        print("Result: Strong Password")

    else:
        print("Result: Weak Password")
        print("Missing Criteria:")

        if len(password) < 8:
            print("- At least 8 characters long")

        if not has_uppercase:
            print("- At least one uppercase letter")

        if not has_lowercase:
            print("- At least one lowercase letter")

        if not has_digit:
            print("- At least one digit")

        if not has_special:
            print("- At least one special character (!@#$%^&*)")