import json

class IDCard:
    def __init__(self, employee):
        self.employee = employee

    def show_id_card(self):
        print("=== ID Card ===")
        print(f"Employee ID: {self.employee.employee_id}")
        print(f"Name: {self.employee.name}")
        print(f"Role: {self.employee.role}")
        print(f"Salary: {self.employee.salary:.2f}")


class Employee:
    def __init__(self, employee_id, role: str, salary: float):
        self._employee_id = employee_id
        self._salary = salary
        self._role = role

    @property
    def employee_id(self):
        return self._employee_id

    @property
    def salary(self):
        return self._salary

    @property
    def role(self):
        return self._role


class Engineer(Employee):
    def __init__(self, employee_id, name: str, role: str, salary: float):
        super().__init__(employee_id, role, salary)
        self._name = name

    @property
    def name(self):
        return self._name

    def show_details(self):
        """Prints details of the engineer."""
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Salary: {self.salary:.2f}")


def save_engineer_details(engineer):
    try:
        with open("engineer_details.json", "w") as f:
            json.dump({"employee_id": engineer.employee_id, "name": engineer.name, "role": engineer.role, "salary": engineer.salary}, f)
        print("Engineer details saved successfully.")
    except Exception as e:
        print(f"Error saving engineer details: {e}")


def load_engineer_details(employee_id):
    try:
        with open("engineer_details.json", "r") as f:
            data = json.load(f)
            if data["employee_id"] == employee_id:
                return Engineer(data["employee_id"], data["name"], data["role"], data["salary"])
            else:
                print("No engineer details found for the provided employee ID.")
                return None
    except FileNotFoundError:
        print("No engineer details found.")
        return None
    except Exception as e:
        print(f"Error loading engineer details: {e}")
        return None


def main():
    action = input("Do you want to create an ID card or get an ID card? (create/get): ")

    if action == "create":
        try:
            employee_id = input("Enter the employee ID: ")
            name = input("Enter the name of the engineer: ")
            role = input("Enter the role of the engineer: ")
            salary = float(input("Enter the salary of the engineer: "))
            engineer = Engineer(employee_id, name, role, salary)
            save_engineer_details(engineer)
        except ValueError:
            print("Invalid input. Please enter valid values.")
    elif action == "get":
        employee_id = input("Enter the employee ID whose ID card you want to get: ")
        engineer = load_engineer_details(employee_id)
        if engineer:
            id_card = IDCard(engineer)
            id_card.show_id_card()
        else:
            print("No engineer details available for the provided employee ID.")


if __name__ == "__main__":
    main()