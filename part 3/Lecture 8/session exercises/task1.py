class Employer:
    def __init__(self,name,employer_id,basic_salary):
        self.name=name
        self.employer_id=employer_id
        self.basic_salary=basic_salary
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employer: {self.employer_id}")
        print(f"Salary: {self.basic_salary}")
    def calculate_salary(self):
        return self.basic_salary
class Developer(Employer):
    def __init__(self,name,employer_id,basic_salary,programming_language):
        super().__init__(name,employer_id,basic_salary)
        self.programming_language=programming_language
    def calculate_salary(self):
        return self.basic_salary+5000
    def display_developer_details(self):
        print(f"Name: {self.name}")
        print(f"Employer: {self.employer_id}")
        print(f"Salary: {self.calculate_salary()}")
        print(f"Programming language: {self.programming_language}")

y=Employer("Rahul","E101",40000)
y.display_details()
x=Developer("Rahul","E101",40000,"Python")
x.display_developer_details()