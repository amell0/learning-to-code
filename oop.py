class student:
    def __init__(self, fname, lname, grade):
        self.fname = fname
        self.lname = lname
        self.grade = grade

student1 = student("Amel", "Lounici", "11.36")
print(student1.fname, student1.lname)