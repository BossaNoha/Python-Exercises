class StudentGrade_Manager:
    def __init__(self):
        self.students_gradelist = {}
        self.averages_of_students = {}

    def my_UI(self):
        my_input = ""
        while my_input != "quit":
            print("List of options: \n add student \n add grade \n show average grades of all students (type 'averages') \n show top student(s) (type 'tops')\n quit")
            my_input = input("What would you like to do?").lower()
            if my_input == "add student":
                student_name = self.pick_student()
                self.add_student(student_name)
            elif my_input == "add grade":
                student_name = self.pick_student()
                self.add_grade(student_name)
            elif my_input == "averages":
                if self.students_gradelist != {}:
                    self.averagator()
                    self.show_students_averages()
                else: print("There haven't been added any students yet")
            elif my_input == "tops":
                if self.students_gradelist != {}:
                    self.averagator()
                    self.show_top_students()
                else: print("There haven't been added any students yet")
            elif my_input == "quit": print("quitting")
            else: print ("invalid input")
                

    def pick_student(self):
        students_name = input("Insert name of the student")
        return students_name

    def add_student(self, students_name):
        students_grades = []
        self.students_gradelist[students_name] = students_grades

    def add_grade(self, students_name):
        if students_name not in self.students_gradelist: print(f"{students_name} wasnt added yet")
        else:
            students_grade = int(input(f"Insert new grade of {students_name}"))
            self.students_gradelist[students_name].append(students_grade)

    def averagator(self):
        for student in self.students_gradelist:
            averaging = 0
            for grade in self.students_gradelist[student]:
                averaging += grade
            averaged = averaging/len(self.students_gradelist[student])
            self.averages_of_students[student] = averaged
    
    def show_students_averages(self):
        print (self.averages_of_students)
    
    def show_top_students(self):
        max_average = max(self.averages_of_students.values())
        top_students = [student for student, avg in self.averages_of_students.items() if avg == max_average]
        print(f"Top student(s) with average {max_average}: {top_students}")


sgm = StudentGrade_Manager()
sgm.my_UI()