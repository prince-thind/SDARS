import os
import pickle


# ======================================================================================================================
class circulars:
    def __init__(self, student_class: str):
        self.student_class = student_class
        self.data = {}
        self.make_circular_dir()

    def make_circular_dir(self):
        self.path = "C:\\Users\\Sumit\\PycharmProjects\\csproject\\circular_class{}".format(self.student_class)
        directory = os.listdir(path=self.path)
        self.directory = []
        for i in directory:
            if i.endswith(".dat"):
                self.directory.append(i)
            else:
                continue

    def get_data(self):
        for file_name in self.directory:
            # there is a great chance of server breakdown at this point, because in case there are many circulars the
            # whole server could experience a great ram usage and lag.
            with open(file_name, "rb") as file_obj:
                data = pickle.load(file_obj).copy()
            self.data[file_name] = data.copy()
            data.clear()

        return self.data

    def last_circular_no(self):
        return int(self.directory[-1].replace(".dat", "").replace("circular_no", ""))


# =======================================================================================================================

class assignments:
    def __init__(self, class_n_sec: str):
        self.class_n_sec = class_n_sec
        self.make_assgn_dir()
        self.total_data = {}

    def make_assgn_dir(self):
        self.path = 'C:\\Users\\Sumit\\PycharmProjects\\csproject\\assignments_{}'.format(self.class_n_sec)
        directory = os.listdir(path=self.path)
        self.directory = []
        for i in directory:
            if i.endswith(".txt"):
                self.directory.append(i)
            else:
                continue

    def get_data(self):
        for file in self.directory:
            # there is a great chance of server breakdown at this point, because in case there are many assignments the
            # whole server could experience a great ram usage and lag.
            file_obj = open(file, "r")
            self.total_data[file] = file_obj.readlines()
        return self.total_data.copy()

    def last_assgn_no(self):
        num = int(self.directory[-1].replace(".txt", "").replace("assignment", ""))
        return num
