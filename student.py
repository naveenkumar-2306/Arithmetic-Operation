def filewrite(name, g = -1):
    with open("file1.txt",'a') as f:
        if g == -1:
            text = name
            f.write(f"name: {text}\n")
            f.write("Courses:\n")
        else:
            co = name
            grad = g
            f.write(f"Course: {co}, grade: {grad}\n")

def filewrite1(cg):
    with open("file1.txt", 'a') as f:
        f.write(f"CGPA: {cg}\n")
        f.write("___________________________________________________\n\n")
class person():
    def __init__(self, name):
        self.name = name
        filewrite(name)
    def display(self):
        print(f"name: {self.name}")


class Course():
    def __init__(self, course, grade):
        self.course = course
        self.grade = grade


class Student(person):
    def __init__(self,name):
        super().__init__(name)
        self.courses = []
    def assignname(self,name):
        person(name)
    def addnewstud(self):
        c = 'y'
        while (c == 'y' or c == 'Y'):
            cname = input("Enter course name ")
            cgrade = int(input("Enter grade "))
            c = input("Do you want to add course? (y/n)")
            Course(cname, cgrade)
            filewrite(cname,cgrade)
            self.courses.append(Course(cname, cgrade))

    def calgrade(self):
        summ = 0
        siz = len(self.courses)
        for g in self.courses:
            summ = summ + g.grade
        cgpa = summ / siz
        return cgpa

    def display(self):
        print("Courses")
        for j in self.courses:
            print(f"Course: {j.course}, grade: {j.grade}")
        print(f"cgpa: {self.calgrade()}")
        print("____________________________________\n\n")


students = []
n = int(input("Enter num of students "))
for i in range(n):
    na = input(f"Enter the name {i+1} of student ")
    c1 = Student(na)
    c1.addnewstud()
    filewrite1(c1.calgrade())
    students.append(c1)

choice = int(input("Enter the choice\n1.display\t2.add new student\t3.exit "))
while(choice != 3):
    if choice == 1:
        for k in students:
            p1 = person(k.name)
            p1.display()
            print("--------------------")
            k.display()
        choice = int(input("Enter the choice\n1.display\t2.add new student\t3.exit "))

    elif choice == 2:
        na = input(f"Enter the name of student")
        c1 = Student(na)
        c1.addnewstud()
        students.append(c1)
        choice = int(input("Enter the choice\n1.display\t2.add new student\t3.exit "))
    else:
        print("Sorry wrong choice, Please enter again")
        choice = int(input("Enter the choice\n1.display\t2.add new student\t3.exit "))

if choice == 3:
    print("Thank you, bye for now")


