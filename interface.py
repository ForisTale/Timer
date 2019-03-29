def initialize(timer, database):
    opening_text = "Please write command, if need help, write \"help\" for list of commands.\n "

    while True:
        inp = input(opening_text).lower()

        if inp == "auto":
            automatic_execution(timer, database)
        elif inp == "start_time":
            start_count_time(timer)
        elif inp == "end_time":
            end_count_time(timer)
        elif inp == "comment":
            write_comment(timer)
        elif inp == "tag":
            tag(timer)
        elif inp == "id":
            set_id(timer, database)
        elif inp == "read":
            print_records(database)
        elif inp == "save":
            save(timer, database)
        elif inp == "close":
            break
        elif inp == "help":
            print_commands()
        else:
            print(dont_recognize_text())


def automatic_execution(timer, database):
    timer.reset_data()
    timer.start()
    while True:
        input("Press ENTER to ends the time counting.")
        q = input("Are you sure that you want to ends the time "
                  "counting?\nWrite \"y\" if yes. ")
        if q == "y" or q == "Y":
            break
    timer.end()
    timer.write_comment()
    timer.mark_tags()
    timer.set_data()
    database.add_entry(timer.data)


def start_count_time(timer):
    timer.start()


def end_count_time(timer):
    timer.end()


def write_comment(timer):
    timer.write_comment()


def tag(timer):
    timer.mark_tags()


def set_id(timer, database):
    timer.set_id()
    if database.id_is_in_use(timer.id):
        print(
            "This id: {} is in use, if you don't set other id, "
            "id will change automatically when save.".format(timer.id))
    else:
        print("Id was set to {}.".format(timer.id))


def print_records(database):
    while True:
        choice = input("Please choice read mode, available modes:"
                       "\n\"all\" see all entry's."
                       "\n\"last\" see last entry"
                       "\n\"few\" see last few entry's, you choice how many.\n")
        if choice == "all":
            print(database.read_database())
            enter_to_continue()
            break
        elif choice == "last":
            print(database.read_database(1))
            enter_to_continue()
            break
        elif choice == "few":
            amount = input("Please write how many records you want to see: ")
            print(database.read_database(int(amount)))
            enter_to_continue()
            break
        elif choice == "help":
            pass
        else:
            print(dont_recognize_text()[:30] + ".")


def save(timer, database):
    database.add_entry(timer.data)
    timer.reset_data()


def print_commands():
    print("Commands are:"
          "\n\"auto\" for start program automatically."
          "\nCommands for manual usage:"
          "\n\"start_time\" for starting time count."
          "\n\"end_time\" for end time count."
          "\n\"comment\" for add comment."
          "\n\"tag\" for add tags."
          "\n\"id\" for chose id number."
          "\n\"read\" for see session entry"
          "\n\"save\" for saving session"
          "\n\"close\" for closing program.")


def enter_to_continue():
    input("Press enter to continue.")


def dont_recognize_text():
    return "I don't recognise this command, for commands list use \"help\""
