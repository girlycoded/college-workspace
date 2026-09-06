# name: joosan tibbetts
# desc: hotel reservation system

#consts
MENU_CHOICE_MESSAGE = "Hotel Reservation System\n 1. Enter Reservation\n 2. Display Room Chart\n 3. Exit\nEnter choice: "

## vars
reservation_count = 0
choice = 0
nights = 0
name = ""
room_type = ""

while True:
    menu_choice = input(MENU_CHOICE_MESSAGE).lower().strip()

    if menu_choice == "1":
        name = input("Guest Name: ")
        while True:
            room_type = input("Enter room type (S for single, D for double): ")
            if room_type != "s" and room_type != "d": 
                print("Invalid Selection") 
            else: break
        while True:
            nights = int(input("Enter amount of nights: "))
            if nights <= 0: 
                print("Invalid number of nights. Nights must be greater than zero.")
            else: break
        reservation_count += 1

        print(f"Reservation Summary\n Name: {name}\n Room Type: {room_type}\n Night amount: {nights}")
        input("Press enter to continue...")
    elif menu_choice == "2":
        print("\nRoom Chart", end="")
        for floor in range(4, 0, -1):
            print(f"\n{floor}.  ", end = "")
            for room_number in range(1, 6):
                print(str(floor * 100 + room_number) + " ", end = "")
        print("\n")
    elif menu_choice == "3":
        print(f"Reservations made: {reservation_count}\nThankyou! Have a good day! .w.")
        break
    else:
        input("Invalid menu option. Press enter to continue...")