#!/usr/bin/python3
""" This script uses REST API to retrieve the task completed
    by all employees, then exports it to a json file """

import json
import requests


def toDo():
    """ Function exports all employees to a json file """
    todo_dict = {}

    emp_url = "https://jsonplaceholder.typicode.com/users"
    emp_response = requests.get(emp_url)

    if emp_response.status_code == 200:
        emp_data = emp_response.json()

        for item in emp_data:
            emp_id = item['id']
            usr_name = item['username']

            todo_url = f"https://jsonplaceholder.typicode.com" \
                       f"/users/{emp_id}/todos"
            todo_response = requests.get(todo_url)

            if todo_response.status_code == 200:
                todo_data = todo_response.json()
                todo_list = []

                for item in todo_data:
                    todo_list.append({
                        "username": usr_name,
                        "task": item['title'],
                        "completed": item['completed']
                    })
                todo_dict[emp_id] = todo_list

            else:
                print("Error: Unable to fetch todo data.")

    else:
        print("Error: Unable to fetch user data.")

    with open(f'todo_all_employees.json', mode='w', newline='') as file:
        json.dump(todo_dict, file)


if __name__ == "__main__":
    toDo()
