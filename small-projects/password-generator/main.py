from secrets import choice, SystemRandom
from string import ascii_lowercase, ascii_uppercase, digits


print("Welcome to Password Generator X10XJ")
print("""
- simple mode: type length to generate password
- advance mode: - advance mode: choose how many of each character type to include
- password must be >= 8
""")

VALID_MODES = ("simple", "advance")
CHARACTER_POOLS = {
    "special_case": ["!", "@", "#", "$", "%", "*", "&", "(", ")"],
    "upper_case": ascii_uppercase,
    "lower_case": ascii_lowercase,
    "digits": digits
}
MIN_LENGTH = 8  # sets the minimum length for the password
MAX_LENGTH = MAX_COUNT = 128


def parse_length(raw_input):
    try:
        length = int(raw_input)
    except ValueError:
        print("Please enter a valid number :)")
        return None
    if length < MIN_LENGTH:
        print(f"Password must be >= {MIN_LENGTH}")
        return None
    if length > MAX_LENGTH:
        print(f"Password must be <= {MAX_LENGTH}")
        return None
    return length


def generate_simple_password(length):
    char_list = []
    still_building = True
    while still_building:
        for pool in CHARACTER_POOLS.values():
            char_list.append(choice(pool))
            if len(char_list) >= length:
                still_building = False
                break
    SystemRandom().shuffle(char_list)
    return "".join(char_list)


def run_simple_mode():
    raw_length = input("Enter the length of the password: ")
    length = parse_length(raw_length)
    if length is not None:
        print("Here are the random 7 passwords for you:")
        for index in range(7):
            print(f"{index+1} -> {generate_simple_password(length)}")


def ask_count(prompt):
    while True:
        raw_count = input(prompt).strip()
        try:
            count = int(raw_count)
        except ValueError:
            print("Please enter a valid number!")
            continue
        if count < 0:
            print("You can't use a negative number!")
            continue
        if count > MAX_COUNT:
            print(f"Count can't exceed {MAX_COUNT}.")
            continue
        return count


def collect_counts():
    special_count = ask_count("How many special character: ")
    digit_count = ask_count("How many digits should be in pass: ")
    lower_count = ask_count("How many lower case character: ")
    upper_count = ask_count("How many upper case character: ")
    return special_count, digit_count, lower_count, upper_count


def build_advance_password(counts):
    special_count, digit_count, lower_count, upper_count = counts
    char_list = []

    for _ in range(special_count):
        char_list.append(choice(CHARACTER_POOLS["special_case"]))
    for _ in range(digit_count):
        char_list.append(choice(CHARACTER_POOLS["digits"]))
    for _ in range(lower_count):
        char_list.append(choice(CHARACTER_POOLS["lower_case"]))
    for _ in range(upper_count):
        char_list.append(choice(CHARACTER_POOLS["upper_case"]))

    SystemRandom().shuffle(char_list)
    return "".join(char_list)


def run_advance_mode():
    counts = collect_counts()
    total = sum(counts)
    if total < MIN_LENGTH:
        print(f"Password must be >= {MIN_LENGTH} (got {total})")
        return
    if total > MAX_LENGTH:
        print(f"Total length must be <= {MAX_LENGTH} (got {total})")
        return

    print("Here are your 6 passwords based on your combination:")
    for index in range(6):
        print(f"{index+1} -> {build_advance_password(counts)}")


def get_mode():
    for _ in range(10):
        mode = input("simple/advance: ").strip().lower()
        if mode in VALID_MODES:
            return mode
        print("Choose between simple/advance\n")
    print("You are out of chances to generate password :(")
    return None


if __name__ == "__main__":
    try:
        mode = get_mode()
        if mode == VALID_MODES[0]:
            run_simple_mode()
        elif mode == VALID_MODES[1]:
            run_advance_mode()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
