import random
import time
import os
import shutil

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_width():
    return shutil.get_terminal_size().columns

def center(text):
    """Print a line centered on the terminal."""
    print(text.center(get_width()))

def center_plain(text):
    """Center plain text (no color codes affect width)."""
    w = get_width()
    print(text.center(w))

WORDS = [
    ("python",      "A popular programming language"),
    ("developer",   "Someone who writes code"),
    ("internship",  "A training program at a company"),
    ("keyboard",    "You type on this"),
    ("algorithm",   "A set of steps to solve a problem"),
]

STAGES = [
"""\
+-------+
|       |
        |
        |
        |
        |
        |
=========""",
"""\
+-------+
|       |
O       |
        |
        |
        |
        |
=========""",
"""\
+-------+
|       |
O       |
|       |
        |
        |
        |
=========""",
"""\
+-------+
|       |
O       |
/|      |
        |
        |
        |
=========""",
"""\
+-------+
|       |
O       |
/|\\     |
        |
        |
        |
=========""",
"""\
+-------+
|       |
O       |
/|\\     |
/       |
        |
        |
=========""",
"""\
+-------+
|       |
O       |
/|\\     |
/ \\     |
        |
        |
=========""",
]

MAX_WRONG = 6

RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

def print_banner():
    w = get_width()
    lines = [
        r"██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗",
        r"██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║",
        r"███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║",
        r"██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║",
        r"██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║",
        r"╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝",
    ]
    print()
    for line in lines:
        pad = max(0, (w - len(line)) // 2) * " "
        print(f"{pad}{CYAN}{BOLD}{line}{RESET}")
    print()

def print_hangman(wrong):
    """Print the hangman drawing centered on screen."""
    w = get_width()
    lines = STAGES[wrong].split("\n")
    for line in lines:
        pad = max(0, (w - 9) // 2) * " "   # 9 = width of drawing
        print(f"{pad}{WHITE}{line}{RESET}")
    print()

def print_status(word, guessed, wrong, hint):
    w = get_width()

    # Word display
    display = "   ".join(
        f"{GREEN}{BOLD}{ch.upper()}{RESET}" if ch in guessed else f"{YELLOW}_{RESET}"
        for ch in word
    )
    # Strip color codes to get real length for centering
    plain_display = "   ".join(ch.upper() if ch in guessed else "_" for ch in word)
    pad = max(0, (w - len(plain_display) - 10) // 2) * " "
    print(f"{pad}{BOLD}Word  :{RESET}  {display}")

    # Hint
    hint_line = f"Hint  :  {hint}"
    pad2 = max(0, (w - len(hint_line)) // 2) * " "
    print(f"{pad2}{BOLD}Hint  :{RESET}  {hint}")

    # Lives
    hearts = "❤️  " * (MAX_WRONG - wrong) + "🖤 " * wrong
    lives_label = "Lives :  "
    pad3 = max(0, (w - len(lives_label) - (MAX_WRONG * 3)) // 2) * " "
    print(f"{pad3}{BOLD}Lives :{RESET}  {hearts}")

    # Tried letters
    if guessed:
        tried = "  ".join(
            f"{GREEN}{ch}{RESET}" if ch in word else f"{RED}{ch}{RESET}"
            for ch in sorted(guessed)
        )
        plain_tried = "  ".join(ch for ch in sorted(guessed))
        pad4 = max(0, (w - len(plain_tried) - 10) // 2) * " "
        print(f"{pad4}{BOLD}Tried :{RESET}  {tried}")

    print()

def centered_input(prompt):
    w = get_width()
    pad = max(0, (w - len(prompt) - 20) // 2) * " "
    return input(f"{pad}{prompt}").strip().lower()

def play():
    clear()
    print_banner()
    time.sleep(1)

    word, hint = random.choice(WORDS)
    guessed    = set()
    wrong      = 0

    w = get_width()
    msg = f"A new word chosen! You have {MAX_WRONG} lives."
    print(f"{msg.center(w)}")
    print()
    time.sleep(1)

    while wrong < MAX_WRONG:
        clear()
        print_banner()
        print_hangman(wrong)
        print_status(word, guessed, wrong, hint)

        # Win check
        if all(ch in guessed for ch in word):
            score = (MAX_WRONG - wrong) * 10
            win_msg = f"YOU WON!  The word was '{word.upper()}'"
            score_msg = f"Score: {score} points!"
            print(f"{GREEN}{BOLD}{win_msg.center(get_width())}{RESET}")
            print(f"{CYAN}{score_msg.center(get_width())}{RESET}")
            print()
            return True, score

        guess = centered_input(f"{BOLD}Enter a letter: {RESET}")

        if len(guess) != 1 or not guess.isalpha():
            msg = "Please enter a single letter!"
            print(f"{RED}{msg.center(get_width())}{RESET}")
            time.sleep(1)
            continue

        if guess in guessed:
            msg = f"You already tried '{guess}'!"
            print(f"{YELLOW}{msg.center(get_width())}{RESET}")
            time.sleep(1)
            continue

        guessed.add(guess)

        if guess in word:
            msg = f"'{guess}' is in the word! Great guess!"
            print(f"{GREEN}{msg.center(get_width())}{RESET}")
        else:
            wrong += 1
            msg = f"'{guess}' is NOT in the word! {MAX_WRONG - wrong} lives left."
            print(f"{RED}{msg.center(get_width())}{RESET}")
        time.sleep(1)

    # Lose
    clear()
    print_banner()
    print_hangman(wrong)
    print_status(word, guessed, wrong, hint)
    lose_msg = f"GAME OVER!  The word was '{word.upper()}'"
    print(f"{RED}{BOLD}{lose_msg.center(get_width())}{RESET}")
    print()
    return False, 0

def main():
    total_score = 0
    wins  = 0
    games = 0

    while True:
        won, score = play()
        games += 1
        if won:
            wins       += 1
            total_score += score

        w = get_width()
        stats = f"Stats  ->  Wins: {wins}/{games}   |   Total Score: {total_score}"
        print(f"{CYAN}{stats.center(w)}{RESET}")
        print()
        again = centered_input(f"{BOLD}Play again? (y/n): {RESET}")
        if again != "y":
            clear()
            print_banner()
            print(f"{CYAN}{BOLD}{'Thanks for playing Hangman!'.center(get_width())}{RESET}")
            print(f"{YELLOW}{'Final Score : ' + str(total_score) + ' points'.center(get_width())}{RESET}")
            print(f"{YELLOW}{'Games Won   : ' + str(wins) + '/' + str(games)}{RESET}".center(get_width()))
            print()
            break

if __name__ == "__main__":
    main()
