class Interface:
    def __init__(self, timer, database):
        self.timer = timer
        self.database = database

    def initialize(self):
        """
        TODO check if you can use execute instead of if
        """
        text = "Please write command, if need help, write \"help\" for list of commands.\n "
        dont_recognize_text = "I don't recognise this command, for commands list use \"help\""

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
                self.timer.start()
                while True:
                    input("Press ENTER to ends the time counting.")
                    q = input("Are you sure that you want to ends the time "
                              "counting?\nWrite \"y\" if yes. ")
                    if q == "y" or q == "Y":
                        break
                self.timer.end()
                self.timer.comment()
                self.timer.add_tags()
                self.timer.set_data()
                self.database.add_entry(self.timer.data)
                self.timer.reset_data()
                self.timer.reset_tags()

            elif inp == "start_time":
                self.timer.start()
            elif inp == "end_time":
                self.timer.end()
            elif inp == "comment":
                self.timer.comment()
            elif inp == "tag":
                self.timer.add_tags()
            elif inp == "id":
                self.timer.set_id()
                if not self.database.check_id(self.timer.id):
                    print(
                        "This id: {} is in use, if you don't set other id, "
                        "id will change automatically when save.".format(self.timer.id))
                else:
                    print("Id was set to {}.".format(self.timer.id))
            elif inp == "read":
                while True:
                    choice = input("Please choice read mode, available modes:"
                                   "\n\"all\" see all entry's."
                                   "\n\"last\" see last entry"
                                   "\n\"few\" see last few entry's, you choice how many.\n")
                    if choice == "all":
                        print(self.database.read())
                        self.enter_to_continue()
                        break
                    elif choice == "last":
                        print(self.database.read(1))
                        self.enter_to_continue()
                        break
                    elif choice == "few":
                        amount = input("Please write how many records you want to see: ")
                        try:
                            print(self.database.read(int(amount)))
                            self.enter_to_continue()
                            break
                        except ValueError:
                            print("Need to be number!")
                            self.enter_to_continue()
                    elif choice == "help":
                        pass
                    else:
                        print(dont_recognize_text[:30]+".")
                        self.enter_to_continue()
            elif inp == "save":
                self.database.add_entry(self.timer.data)
                self.timer.reset_data()
            elif inp == "close":
                break
            elif inp == "help":
                print(help_txt)
            else:
                print(dont_recognize_text)

    @staticmethod
    def enter_to_continue():
        input("Press enter to continue.")
