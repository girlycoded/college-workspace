#name: joosan tibbetts
#desc: use a dictionary to provide iPhone support

user_prompt = ""

problems = {
    "no_response": "Please charge the iPhone",
    "App doesn't work": "Please update the app",
    "Lines through the image": "Please replace your screen",
    "Dropped into water": "Soak it in rice",
    "Won't unlock": "Replace the battery",
    "Other": "Buy a new iPhone"
}

def greeting():
    try:
        return int(input(user_prompt))
    except: pass

def closing():
    print("Goodbye have a wonderfully apple day!")

def init():
    global user_prompt
    index = 0
    for issue in problems.keys():
        index += 1
        user_prompt += f"{index}. {issue} \n"
    user_prompt += "Hello world! Welcome to iPhone support. Enter the number corresponding with your issue. Enter nothing to quit: "

    while True:
        do_continue = main()
        if not do_continue: closing(); return

def main():
    option = greeting()
    if not option: return

    try:
        input(f"Solution: {list(problems.values())[option - 1]}")
    except: pass

    return True

init()