import time

from GradeBook import Grade

def main():
    marks = Grade()
    while True:
        print("Welcome! to your Gradebook app."
              "\n 1.View student grades \n 2.Add student grade \n 3.Update student grade \n 4.View Average grades"
              "\n 5.Search for student \n 6.Quit")
        option = int(input('>'))
        if option == 1:
            time.sleep(1)
            marks.view_grades()

        elif option == 2:
            print("Enter name of Student: ")
            NM = input('>')
            time.sleep(0.5)
            try:
                print("Enter student's grade(0-100): ")
                gd = float(input('>'))
                if gd > 100:
                    return "Error! grade must be between 0-100!"
                else:
                    marks.add_student(NM, gd)
                    print(f"{NM}'s grade added successfully")
            except ValueError:
                print("Enter numbers only!")

        elif option == 3:
            marks.view_grades()
            time.sleep(0.5)
            print("Select student grade to update by entering student's name. \n Enter student name: ")
            NM = input('>')
            time.sleep(0.5)
            try:
                print("Enter new grade: ")
                ngd = float(input('>'))
                if ngd > 100:
                    return "Error! grade must be between 0-100!"
                else:
                    marks.update_grade(NM, ngd)
            except ValueError:
                print("Enter numbers only!")

        elif option == 4:
            marks.average_score()
            time.sleep(1)

        elif option == 5:
            print("Search by entering student's name: ")
            query = input('>')
            time.sleep(0.5)
            marks.search(query)

        elif option == 6:
            break


main()

