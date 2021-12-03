# INHERITANCE :-
# The method of inheriting the properties of Parent class into Child class is called inheritance
# (or) creating an relationship between two classes is called inheritance.
class Employee:
    def basic_details(self):
        Name = input('enter employee name: ')
        id = int(input('enter employee id number: '))
        print('name of the employee: ',Name)
        print('id of the employee: ',id)
class Manager(Employee):
    def Calculatem(self):
        Basic_salary = float(input('enter the basic salary: '))
        Hra = 10%Basic_salary
        print('manager salary: ',Hra)
class Labor(Manager):
    def Calculatel(self):
        Basic_salary = float(input('enter the basic salary: '))
        Hra = 3%Basic_salary
        print('labor salary: ',Hra)
class Officestaff(Labor):
    def Calculateo(self):
        Basic_salary = float(input('enter the basic salary: '))
        Hra = 7%Basic_salary
        print('office staff salary: ',Hra)
sai = Officestaff()
sai.basic_details()
sai.Calculatem()
sai.Calculatel()
sai.Calculateo()