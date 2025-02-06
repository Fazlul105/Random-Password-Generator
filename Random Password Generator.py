import secrets
import string


def get_valid_length():
    while True:
        try:
            length = int(input("Enter password length (8-64): "))
            if 8 <= length <= 64:
                return length
            print("Length must be between 8 and 64.")
        except ValueError:
            print("Invalid input. Enter a number.")


def get_character_sets():
    sets = {
        'letters': string.ascii_letters,
        'numbers': string.digits,
        'symbols': string.punctuation
    }
    chosen = []

    print("Select character types:")
    for key in sets:
        if input(f"Include {key}? (y/n): ").lower() == 'y':
            chosen.append(sets[key])

    if not chosen:
        print("At least one character type must be selected!")
        return get_character_sets()
    return ''.join(chosen)


def generate_password():
    print("=== Random Password Generator ===")
    length = get_valid_length()
    chars = get_character_sets()
    password = ''.join(secrets.choice(chars) for _ in range(length))
    print(f"\nGenerated Password: {password}")


if __name__ == "__main__":
    generate_password()