class Student:
    grade = 10

    def __init__(self, grade=None):
        if grade is not None:
            self.grade = grade

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student()
print("Hi I am a student of grade", student.grade)


model_x = Vehicle(240, 18)
print("Model Max Speed:", model_x.max_speed)
print("Model Mileage:", model_x.mileage)


blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))