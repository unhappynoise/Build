import json
import os.path



class Grade:

    def __init__(self):
        self.students = {}
        self.load_grades()

    def save_grade(self):
        grade = {"Students": self.students}
        with open("grade_app.json", "w") as file:
            json.dump(grade, file, indent=3)


    def load_grades(self):
        try:
            if os.path.exists("grade_app.json"):
                with open("grade_app.json", "r") as file:
                    grade = json.load(file)
                    self.students = grade.get("Students", {})

            else:
                self.students = {}

        except FileNotFoundError:
            print("No records of Students and grades yet. \n Add students with grade and save to automatically create the file")


    def add_student(self, name, grade):
        self.students[name] = grade
        self.save_grade()

    def view_grades(self):
        if not self.students:
            print("No grade records yet.")
        else:
            arranged = sorted(self.students.items(), key=lambda x: x[1], reverse=True)

            for student, grade in arranged:
                print(f"{student} : {grade}")

    def update_grade(self, name, new_grade):
        if name in self.students:
            self.students[name] = new_grade
            self.save_grade()
            print(f"{name}'s grade updated to {new_grade}.")
        else:
            print(f"{name} not found.")

    def search(self, query):
        found = False

        if query in self.students:
            print(f"{query}: {self.students[query]}")
            found = True

        if not found:
            print("There's no name as such here.")

    def average_score(self):
        total = sum(self.students.values())
        count = len(self.students)

        average = total / count
        print(f"The class average is: {average:.2f}")
