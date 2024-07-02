import re
def check_password_strength(password):

    strength = 0
    feedback = []
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))

    if length_criteria:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if uppercase_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if lowercase_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if digit_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one digit.")

    if special_char_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    if strength == 5:
        feedback.append("Password is very strong.")
    elif strength >= 3:
        feedback.append("Password is strong.")
    elif strength >= 1:
        feedback.append("Password is weak.")
    else:
        feedback.append("Password is very weak.")

    return strength, feedback


def main():
    print("\nPassword Complexity Checker")
    password = input("Enter a password to check its strength: ")
    strength, feedback = check_password_strength(password)

    print("\nPassword Strength Assessment:")
    for comment in feedback:
        print(f"- {comment}")


if __name__ == "__main__":
    main()
