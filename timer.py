import datetime


class Timer:
    """class with purpose to use for measure time
    """

    def __init__(self):
        self.data = {"timer": []}
        self.time = []
        self.comment_full_message = ""
        self.tags = {"python": 0, "sql": 0, "eng": 0, "jap": 0, "other": 0}
        self.id = 0

    def start(self):
        """start time
        """
        self.time = []
        time = datetime.datetime.now()
        self.time.append(time.strftime("%Y-%m-%d %H:%M:%S"))
        print("The program starts counting the time at: "+str(time.time())[0:8])

    def end(self):
        """end time.
        """
        if self.time:
            self.time.append(datetime.datetime.now().strftime
                             ("%Y-%m-%d %H:%M:%S"))
            print("The program ends the time counting.")
        else:
            print("First use command start.")

    def write_comment(self):
        """take comment
        """
        self.comment_full_message = ""
        self.comment_full_message += " " + input("Please write comment: ")

    def mark_tags(self):
        """Take input with tags marks
        """
        t = ""
        for item in self.tags.keys():
            t += item + " "
        text = "Please write tags you want separate by space. Tags you can "\
               "choose are: " + t + "\n "
        inp = input(text)
        inp = inp.split(" ")
        while True:
            index = 0
            for item in inp:
                if item in self.tags:
                    index += 1
                else:
                    print("There is no such tag: " + item)
                    inp = input(text)
                    inp = inp.split(" ")
                    break
            if index == len(inp):
                break
        for item in inp:
            self.tags[item] = 1

    def reset_data(self):
        self.data = {"timer": []}
        for key, value in self.tags.items():
            self.tags[key] = 0

    def set_data(self):
        """set all need data into useful schema
        """
        if self.time:
            combine = {"id": self.id, "start": self.time[0],
                       "end": self.time[1], "comment": self.comment_full_message,
                       **self.tags}
            self.data["timer"].append(combine)
        else:
            print("Please start time count.")

    def set_id(self):
        """allow set id number
        """
        self.id = input("Please write id number for this session: ")
