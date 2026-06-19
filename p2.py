class Student:
    def __init__(self, name, roll_no, age):
        self.name = name
        self.roll_no = roll_no
        self.age = age

    def eating(self):
        print(f"{self.name} is eating.")

    def sleeping(self):
        print(f"{self.name} is sleeping.")

    def playing(self):
        print(f"{self.name} is playing.")

# Create a student object
student1 = Student("john", "R101", 20)
# Call the actions
student1.eating()
student1.sleeping()
student1.playing()

    
