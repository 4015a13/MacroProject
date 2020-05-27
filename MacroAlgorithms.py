# Student object
class Student:
    def __init__(self, name, matGrade, hisGrade, engGrade, spaGrade):
        self.name = name
        self.matGrade = matGrade
        self.hisGrade = hisGrade
        self.engGrade = engGrade
        self.spaGrade = spaGrade

# Register a student
    def register(self):
        Register.append(self)
        print("Operation Successful (REGISTER)")
        print('REGISTER 001')

# Generate grade
    def gengrade(self, grade):
        if grade == "A" or grade == "a":
            return 4.0
        if grade == "B" or grade == "b":
            return 3.2
        if grade == "C" or grade == "c":
            return 2.5
        if grade == "D" or grade == "d":
            return 2.0
        else:
            return 0.0

# Calculate GPA of a student
    def gpa(self):
        return (self.gengrade(self.matGrade) + self.gengrade(self.hisGrade) +
                self.gengrade(self.engGrade) + self.gengrade(self.spaGrade)) / 4.0

# Let you know the student's GPA
    def printGPA(self):
        print(self.name, "'s GPA is:", self.gpa())
        print('GPA 001')

# Let you know how how much aid a student is qualified for BUT does not yet add him in the list
    def status(self):
        if self.gpa() > 3.5:
            print("With a GPA of ", self.gpa(), "the student ",
                  self.name, "is qualified for the full financial aid")
            print('STATUS 001')
        elif 3.5 > self.gpa() >= 3.0:
            print("With a GPA of  ", self.gpa(), " the student ",
                  self.name, " is qualified for half of the financial aid")
            print('STATUS 002')
        elif 3.0 > self.gpa() >= 2.8:
            print("With a GPA of  ", self.gpa(), " the student ",
                  self.name, " is qualified for a quarter of the financial aid")
            print('STATUS 003')
        else:
            print("With a GPA of  ", self.gpa(), " the student ",
                  self.name, " is  not qualified for the financial aid")
            print('STATUS 004')

# Analise student's grades and decide how much aid he's getting and add him to corresponding list
    def evaluate(self):
        if self.gpa() > 3.5:
            fullQualified.append(self)
            print("Student should receive the founds shortly")
            print('EVALUATE 001')
        elif 3.5 > self.gpa() >= 3.0:
            halfQualified.append(self)
            print("Student should receive the founds shortly")
            print('EVALUATE 002')
        elif 3.0 > self.gpa() >= 2.75:
            quarterQualified.append(self)
            print("Student should receive the founds shortly")
            print('EVALUATE 003')
        else:
            notQualified.append(self)
            print("Student will not receive the founds")
            print('EVALUATE 004')

# Force student with a GPA of at least 2.5 into a financial aid receiver
    def force(self):
        if self in notQualified:
            if self.gpa() > 0.0:
                quarterQualified.append(self)
                notQualified.remove(self)
                print("Operation Successful (FORCE)")
                print("Student should receive the founds shortly (FORCED)")
                print('FORCE 001')
        else:
            print("ERROR")
            print('FORCE 002')

# Expel a student from the system
    def expel(self):
        if self in fullQualified:
            Register.remove(self)
            fullQualified.remove(self)
            print("Student expelled")
            print('EXPEL 001')
        elif self in halfQualified:
            Register.remove(self)
            halfQualified.remove(self)
            print("Student expelled")
            print('EXPEL 002')
        elif self in quarterQualified:
            Register.remove(self)
            quarterQualified.remove(self)
            print("Student expelled")
            print('EXPEL 003')
        elif self in notQualified:
            Register.remove(self)
            notQualified.remove(self)
            print("Student expelled")
            print('EXPEL 004')
        else:
            print("ERROR")


# Lists
Register = list()
fullQualified = list()
halfQualified = list()
quarterQualified = list()
notQualified = list()







