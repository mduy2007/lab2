from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, emp_id, name):
        self.emp_id= emp_id
        self.name = name

    # tính lương
    @abstractmethod
    def calculate_salary(self):
        pass

    def __str__(self):
        salary = f"{self.calculate_salary():,}"
        if self.__class__.__name__ == "FullTimeEmployee":
            return f"{self.emp_id} {self.name} FullTime {salary}"
        else:
            return f"{self.emp_id} {self.name} PartTime {salary}"


class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, base_salary, allowance):
        super().__init__(emp_id, name)
        # đóng gói
        self.__base_salary = 0
        self.__allowance= 0
        self.base_salary = base_salary
        self.allowance= allowance

    @property
    def base_salary(self):
        return self.__base_salary

    @base_salary.setter
    def base_salary(self, value):
        # kiểm tra lương
        if value<= 0:
            raise ValueError("Lương cơ bản phải > 0")
        self.__base_salary = value

    @property
    def allowance(self):
        return self.__allowance

    @allowance.setter
    def allowance(self, value):
        # kiểm tra phụ cấp
        if value < 0:
            raise ValueError("Phụ cấp phải >= 0")
        self.__allowance= value

    # tính lương
    def calculate_salary(self):
        return self.__base_salary + self.__allowance

class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hours, rate):
        super().__init__(emp_id, name)
        # đóng gói
        self.__hours= 0
        self.__rate = 0
        self.hours= hours
        self.rate = rate

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        # kiểm tra giờ
        if value < 0:
            raise ValueError("Số giờ phải >= 0")
        self.__hours = value

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, value):
        # kiểm tra đơn giá
        if value< 0:
            raise ValueError("Đơn giá phải >= 0")
        self.__rate= value

    # tính lương
    def calculate_salary(self):
        return self.__hours* self.__rate

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add(self, employee: Employee):
        self.employees.append(employee)

    # tính tổng
    def total_payroll(self):
       
        return sum(emp.calculate_salary() for emp in self.employees)

    def report(self):
        print("=== TVU tech - bảng lương ===")
        for emp in self.employees:
            
            print(str(emp))
        print("-" * 25)
        total = self.total_payroll()
        print(f"tổng quỹ lương: {total:,}")

if __name__ == "__main__":

    my_company = Company("TVU Tech")

    emp1 = FullTimeEmployee("E01", "An", 12_000_000, 2_000_000)
    emp2 = FullTimeEmployee("E02", "Binh", 15_000_000, 1_500_000)
    emp3 = PartTimeEmployee("P01", "Chi", 80, 50_000)

    my_company.add(emp1)
    my_company.add(emp2)
    my_company.add(emp3)

    # in báo cáo
    my_company.report()