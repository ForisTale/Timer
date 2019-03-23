def initialize(t, d):
    """start program data
    """
    text = "Please write command, if need help, write \"help\" for list of commands.\n "
    help_txt = ("Commands are:"
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
    while True:
        inp = input(text).lower()

        if inp == "auto":
            t.start()
            while True:
                input("Press ENTER to ends the time counting.")
                q = input("Are you sure that you want to ends the time "
                          "counting?\nWrite \"y\" if yes. ")
                if q == "y" or q == "Y":
                    break
            t.end()
            t.comment()
            t.add_tags()
            t.set_data()
            d.add_entry(t.data)
            t.reset_data()
            t.reset_tags()

        elif inp == "start_time":
            t.start()
        elif inp == "end_time":
            t.end()
        elif inp == "comment":
            t.comment()
        elif inp == "tag":
            t.add_tags()
        elif inp == "id":
            t.set_id()
            if not d.check_id(t.id):
                print(
                    "This id: {} is in use, if you don't set other id, "
                    "id will change automatically when save.".format(t.id))
            else:
                print("Id was set to {}.".format(t.id))
        elif inp == "read":
            print("Database: ", d.read())
        elif inp == "save":
            d.add_entry(t.data)
            t.reset_data()
        elif inp == "close":
            break
        elif inp == "help":
            print(help_txt)
        else:
            print("I don't recognise this command, for commands list use"  
                  "\"help\"")
