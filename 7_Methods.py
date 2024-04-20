# 2) Class Methods
# 3 ) staic Methods


class Student:
    school = "Sharda"
    
    @classmethod
    def get_school(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("This is student class of abc module")
    

print(Student.get_school())

Student.info()

