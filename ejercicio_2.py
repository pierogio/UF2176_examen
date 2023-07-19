"""2)genera el siguiente ejercicio:
Una clase Employee que tenga los atributos name y salary. La clase también debe tener un método get_salary() que devuelva el salario del empleado y un método change_salary() que cambie el salario del empleado.
Genera la base del script, con (if  __name__) , donde instancies la clase y uses los métodos declarados.
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def change_salary(self, new_salary):
        self.salary = new_salary


if __name__ == "__main__":
    employee = Employee("Piero", 50000000)

    salary = employee.get_salary()
    print(f"El sueldo de {employee.name} es: {salary} eurinis")

    update_salary = 600000000000
    employee.change_salary(update_salary)
    print(f"El nuevo sueldo de {employee.name} es: {employee.get_salary()} eurinis")