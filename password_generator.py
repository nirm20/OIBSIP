"""
Random Password Generator (Beginner Tier)
OIBSIP - Python Programming Internship, Task 3

Generates a random password based on the length and character types
chosen by the user.
"""

import random
import string

MIN_LENGTH = 8


def get_length():
    """Ask for password length. Minimum 8 characters enforced."""
    while True:
        value = input(f"Enter password length (minimum {MIN_LENGTH}): ").strip()
        if not value.isdigit():
            print("Error: please enter a whole number (e.g. 12).")
            continue
        length = int(value)
        if length < MIN_LENGTH:
            print(f"Error: password must be at least {MIN_LENGTH} characters long.")
            continue
        if length > 128:
            print("Error: maximum supported length is 128.")
            continue
        return length


def ask_yes_no(question):
    """Return True for yes, False for no."""
    while True:
        answer = input(question + " (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer with y or n.")


def get_character_types():
    """Ask which character types to include. At least 2 must be selected."""
    while True:
        pools = []
        if ask_yes_no("Include uppercase letters?"):
            pools.append(string.ascii_uppercase)
        if ask_yes_no("Include lowercase letters?"):
            pools.append(string.ascii_lowercase)
        if ask_yes_no("Include numbers?"):
            pools.append(string.digits)
        if ask_yes_no("Include symbols?"):
            pools.append(string.punctuation)

        if len(pools) < 2:
            print("Error: please select at least 2 character types. Try again.\n")
            continue
        return pools


def generate_password(length, pools):
    """Build a password containing at least one character from every chosen type."""
    # one guaranteed character from each selected type
    password = [random.choice(pool) for pool in pools]

    # fill the remaining length from all selected characters combined
    all_chars = "".join(pools)
    password += [random.choice(all_chars) for _ in range(length - len(password))]

    # shuffle so the guaranteed characters are not always at the start
    random.shuffle(password)
    return "".join(password)


def main():
    print("=" * 38)
    print("     RANDOM PASSWORD GENERATOR")
    print("=" * 38)

    while True:
        print()
        length = get_length()
        pools = get_character_types()

        password = generate_password(length, pools)
        print("\nYour generated password:")
        print(f"  {password}")

        if not ask_yes_no("\nGenerate another password?"):
            print("Thank you for using the Password Generator. Stay secure!")
            break


if __name__ == "__main__":
    main()
