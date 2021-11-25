class Student:
    def __init__(self, id, marks):
        self.id = id
        self.marks = marks

    def calculate_average(self):
        total = 0
        for key in self.marks:
            total = total + self.marks[key]
        average = total / len(self.marks)
        return average

    def display_average(self):
        print(self.calculate_average())


if __name__ == '__main__':
    student1 = Student(11888, {'CSF': 75, 'FunPro': 80, 'WT': 85})
    student2 = Student(11111, {'CSF': 65, 'FunPro': 70, 'WT': 75})
    student1.display_average()
    student2.display_average()
    print('test')


# Seminar 10 task 3
class Person:
    def __init__(self, firstName, lastName, birthyear):
        self.firstName = firstName
        self.lastName = lastName
        self.birthyear = birthyear

    def displayName(self):
        print(f'{self.firstName} {self.lastName}')

    def calcAge(self):
        age = 2021 - self.birthyear
        print(age)


john = Person("John", "Smith", 1995)
john.displayName()
john.calcAge()
mark = Person("Mark", "Adams", 1964)
mark.displayName()
mark.calcAge()
mark.calcAge()
