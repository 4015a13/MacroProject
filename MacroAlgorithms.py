class Student:
    def __init__(self, name, matGrade, hisGrade, engGrade, spaGrade):
        self.name = name
        self.matGrade = matGrade
        self.hisGrade = hisGrade
        self.engGrade = engGrade
        self.spaGrade = spaGrade
        self.Register = list()
        self.fullQualified = list()
        self.halfQualified = list()
        self.quarterQualified = list()
        self.notQualified = list()

    def register(self):
        self.Register.append(self)
        print("Operation Successful (REGISTER)")

    def gengrade(self, grade):
        if grade == "A":
            return 4.0
        if grade == "B":
            return 3.2
        if grade == "C":
            return 2.5
        if grade == "D":
            return 2.0
        else:
            return 0.0

    def gpa(self):
        return (self.gengrade(self.matGrade) + self.gengrade(self.hisGrade) +
                self.gengrade(self.engGrade) + self.gengrade(self.spaGrade)) / 4.0

    def status(self):
        if self.gpa() > 3.5:
            print("With a GPA of ",self.gpa(), "the student ",
                  self.name, "is qualified for the financial aid")
        elif 3.5 > self.gpa() >= 3.0:
            print("With a GPA of  ", self.gpa(), " the student ",
                  self.name, " is qualified for half of the financial aid")
        elif 3.0 > self.gpa() >= 2.8:
            print("With a GPA of  ", self.gpa(), " the student ",
                  self.name, " is qualified for a quarter of the financial aid")
        else:
            print("With a GPA of  ", self.gpa(), " the student ",
                  self.name, " is  not qualified for the financial aid")

    def evaluate(self):
        if self in self.Register:
            if self.gpa() > 3.5:
                self.fullQualified.append(self)
                self.Register.remove(self)
                print("Student should receive the founds shortly")
            if 3.5 > self.gpa() >= 3.0:
                self.halfQualified.append(self)
                self.Register.remove(self)
                print("Student should receive the founds shortly")
            if 3.0 > self.gpa() >= 2.8:
                self.quarterQualified.append(self)
                self.Register.remove(self)
                print("Student should receive the founds shortly")
            else:
                self.notQualified.append(self)
                self.Register.remove(self)
                print("Student will not receive the founds")
        else:
            print("Not yet registered")

    def force(self):
        if self in self.notQualified:
            if self.gpa() > 2.5:
                self.quarterQualified.append(self)
                self.notQualified.remove(self)
                print("Operation Successful (FORCE)")
                print("Student should receive the founds shortly (FORCED)")
            else:
                print("Operation Unsuccessful (FORCE)")
                print("Student will not receive the founds (FORCED)")
        else:
            print("ERROR")

    def expel(self):
        if self in self.Register:
            self.Register.remove(self)
            print("Student expelled")
        elif self in self.fullQualified:
            self.fullQualified.remove(self)
            print("Student expelled")
        elif self in self.halfQualified:
            self.halfQualified.remove(self)
            print("Student expelled")
        elif self in self.quarterQualified:
            self.quarterQualified.remove(self)
            print("Student expelled")
        elif self in self.notQualified:
            self.notQualified.remove(self)
            print("Student expelled")
        else:
            print("ERROR")


Ralph = Student("Ralph", "F", "F", "A", "B")

Ralph.register()
Ralph.evaluate()
Ralph.force()
Ralph.expel()





