import csv
import pickle


class Employee:
    def __init__(self, name, vacation_day, vacation_month):
        self.name = name
        self.vacation_day = vacation_day
        self.vacation_month = vacation_month


class VacationChart:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Name', 'Vacation Day', 'Vacation Month'])
            for employee in self.employees:
                writer.writerow([employee.name, employee.vacation_day, employee.vacation_month])

    def save_to_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_from_pickle(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def get_total_employees(self):
        return len(self.employees)

    def get_monthly_vacation_stats(self):
        stats = {}
        for employee in self.employees:
            month = employee.vacation_month
            if month not in stats:
                stats[month] = 0
            stats[month] += 1
        total_employees = self.get_total_employees()
        stats_percentage = {month: count / total_employees * 100 for month, count in stats.items()}
        return stats, stats_percentage

    def search_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                return employee
        return None


def task1():
    data = {
        'employees': [
            {'name': 'Andrei', 'vacation_day': 15, 'vacation_month': 5},
            {'name': 'Nikita', 'vacation_day': 10, 'vacation_month': 7},
            {'name': 'Borys', 'vacation_day': 20, 'vacation_month': 8},
            {'name': 'Alexandr', 'vacation_day': 5, 'vacation_month': 7}
        ]
    }
    vacation_chart = VacationChart()
    for employee_data in data['employees']:
        employee = Employee(employee_data['name'], employee_data['vacation_day'], employee_data['vacation_month'])
        vacation_chart.add_employee(employee)
    vacation_chart.save_to_csv('vacation_chart.csv')
    vacation_chart.save_to_pickle('vacation_chart.pkl')
    loaded_chart = VacationChart.load_from_pickle('vacation_chart.pkl')
    while True:
        choice = int(input("please, choose option : 1 - Total, 2 - Stats, 3 - Found: "))
        match choice:
            case 1:
                total_employees = loaded_chart.get_total_employees()
                print('Total employees:', total_employees)
                return
            case 2:
                stats, stats_percentage = loaded_chart.get_monthly_vacation_stats()
                for month, count in stats.items():
                    print('Month:', month, 'Count:', count, 'Percentage:', stats_percentage[month])
                return
            case 3:
                search_name = input('Enter employee name to search: ')
                found_employee = loaded_chart.search_employee(search_name)
                if found_employee:
                    print('Employee found:')
                    print('Name:', found_employee.name)
                    print('Vacation Day:', found_employee.vacation_day)
                    print('Vacation Month:', found_employee.vacation_month)
                else:
                    print('Employee not found.')
                return
            case _:
                print("incorrect input, please enter one more time: ")




