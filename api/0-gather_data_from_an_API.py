#!/usr/bin/python3
import requests

def get_employee_todo_progress(employee_id):
    """
    function gets todo progress check
    """
    base_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{base_url}/todos?userId={employee_id}"
    user_url = f"{base_url}/users/{employee_id}"

    try:
        """
        Fetch the employee's TODO list
        """
        response = requests.get(todo_url)
        todo_data = response.json()

        '''Fetch the employee's details'''
        response = requests.get(user_url)
        user_data = response.json()
        employee_name = user_data["name"]

        '''Count the number of completed tasks'''
        completed_tasks = [task for task in todo_data if task["completed"]]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todo_data)

        '''Display the progress'''
        print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")

        '''Display the titles of completed tasks'''
        for task in completed_tasks:
            print("\t", task["title"])

    except requests.exceptions.RequestException as e:
        '''handling error'''
        print("Error:", e)

if __name__ == "__main__":
    '''Get the employee ID from the user'''
    try:
        employee_id = int(input("Enter the employee ID: "))
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the employee ID.")
