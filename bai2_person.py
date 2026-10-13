class Person:
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def display_info(self):
        return f'Tên: {self.name}   |   Email: <{self.email}>'

class Student(Person):
    def __init__(self, name, email, student_id, major):
        super().__init__(name, email)
        self.student_id = student_id
        self.major = major

    def display_info(self):
        base = super().display_info()
        base = f'{base}   |   ID: {self.student_id}   |   Nganh: {self.major}'
        return base
        
    def study(self, supject):
        return f"{self.name} Đang Học {supject}"

class Teacher(Person):
    def __init__(self, name, email, department):
        super().__init__(name, email)
        self.department = department

    def display_info(self):
        base = super().display_info()
        base = f'{base}    |    Khoa: {self.department}'
        return base

    def tech(self,subject):
        return f'{self.name} Dạy môn: {subject}'
    
s = Student('Duy','mduy@gmail.com', '001', 'TTNT')
t = Teacher('A', 'ABC123@gmail.com', 'CNTT')

for i in [s,t]:
    print(i.display_info())

print(s.study('OOP'))

print(t.tech('OOP'))