import shutil, os

light_shade = "░"
medium_shade = "▒"
dark_shade = "▓"
full_block = "█" * 32

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def set_cursor_visibility(on: bool):
    print("\033[?25" + ("h" if on else "l"), end="", flush=True)

# start
set_cursor_visibility(False)

size = shutil.get_terminal_size()

while True:
    clear_console()
    for i in range(0, size.lines):
        end_char = "" if i == (size.lines - 1) else "\n"
        print(f"\033[38;2;255;0;0m{light_shade + medium_shade + dark_shade + full_block + dark_shade + medium_shade + light_shade}\033[0m", end=end_char)
    input()
    for i in range(0, size.lines):
        end_char = "" if i == (size.lines - 1) else "\n"
        print(f"\033[38;2;0;255;0m{light_shade + medium_shade + dark_shade + full_block + dark_shade + medium_shade + light_shade}\033[0m", end=end_char)

    input()
    for i in range(0, size.lines):
        end_char = "" if i == (size.lines - 1) else "\n"
        print(f"\033[38;2;0;0;255m{light_shade + medium_shade + dark_shade + full_block + dark_shade + medium_shade + light_shade}\033[0m", end=end_char)
    input()