# welcome text
print("Welcome to your personal todo app!")

# user operation instruction
operation_texts = "\n\tcode:\toperation:\n\t1:\tCreate a task\n\t2:\tMark a task\n\t3:\tDelete a task\n\t4:\tview the list\n\t0:\tExit"

# containter
database = {}
entry_no = 1

# designs


def design():
    print("="*55)


def key_board_interrupt():
    print("\n")  # adds empty line
    print("**Thanks for using the todo-list!**")


def list_update(update="[List updated]"):
    design()
    print(f"\n\t{update}\n")

# operations


def add_entry():
    entry = input("Enter the task: ")
    return database.update({entry_no: entry})


def remove_entry():
    try:
        remove_entry = int(input("Enter the index no to remove: "))
        database.pop(remove_entry)
    except ValueError:
        design()
        print("You have to enter the index!")
        return None
    # re-fining the list
    stop = len(database.keys()) + 1
    for i in range(remove_entry, stop):
        value = database.get(i+1)
        database[i] = value
        database.pop(i+1)
    return 0


def view_list():
    if database:
        design()
        print("\tserial:\ttasks:")
        for key, value in database.items():
            if "[✓]" not in value:
                print(f"\t{key}: \t{value} [x]")
            else:
                print(f"\t{key}: \t{value}")
    else:
        design()
        print("\tCurrently no task is listed!")


RUN = True
while RUN:
    print(operation_texts)

    # user input
    try:
        user_input = int(input("\n(1/2/3/4/0): "))
    except ValueError:
        print("Enter the operation code!")
        continue
    except KeyboardInterrupt:
        key_board_interrupt()
        RUN = False
        continue

    if user_input == 1:
        add_entry()
        list_update()
        entry_no += 1

    elif user_input == 3:
        if database:
            design()
            view_list()
            if remove_entry() == None:
                print("Operation failed!")
            else:
                list_update()
        else:
            design()
            print("\tYou don't have any task to delete!")

    elif user_input == 4:
        view_list()

    elif user_input == 2:
        if database:
            view_list()
            design()
            try:
                mark_input = int(
                    input("Enter the serial of the task to mark: "))
                if mark_input in database.keys():
                    database[mark_input] = f"{database[mark_input]} [✓]"
                    list_update("CONGRATULATIONS 🔥")
                else:
                    design()
                    print("\tIncorrect serial number!")
            except ValueError:
                design()
                print("Please, enter the serial number!")
            except KeyboardInterrupt:
                key_board_interrupt()
                RUN = False
                continue
        else:
            design()
            print("\tYou don't have any task to mark!")

    elif user_input == 0:
        design()
        print("\t**Have a nice day!**")
        RUN = False
    else:
        design()
        print("\tEnter a valid code to operate!")

    design()
