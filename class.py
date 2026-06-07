class Student:
    def __init__(self,name,student_no,course):
        self.name = name
        self.student_no = student_no
        self.course = course

    def study(self,unit):
        print(f"{self.name} studies {unit}.")

    def write(self):
        print(f"{self.name} writes.")

    def participate(self):
        print(f"{self.name} participates.")

    def sleep(self):
        print(f"{self.name} sleeps")

    def get_details(self):
        print("User Details")
        print(f"Name: {self.name} - Student No:{self.student_no} - Course:{self.course}")
        print("________________________________________")

# object 1
student1=Student("Jack","S101","Computer Science")
print(type(student1)) #<class '__main__.Student'>
student1.get_details()
student1.study("Web development")
student1.write()
student1.participate()
student1.sleep()

# Object2
student2=Student("Sophia","S102","Data Science")
print(type(student2))
student2.get_details()
student2.study("Object Oriented Programming")
student2.write()
student2.participate()
student2.sleep()
