#!/usr/bin/python3
""" This script uses REST API to retrieve the task completed
    by a given employee ID """

import requests
from sys import argv


def toDo():
    """ Function retrieves the todos list from api """
    emp_id = int(argv[1])
    todo_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"
    id_response = requests.get(todo_url)

    if id_response.status_code == 200:
        todo_data = id_response.json()
        done_tasks = sum(1 for item in todo_data if item["completed"])
        total_tasks = len(todo_data)

        emp_name_url = "https://jsonplaceholder.typicode.com/users"
        name_response = requests.get(emp_name_url)

        if name_response.status_code == 200:
            name_data = name_response.json()
            for user in name_data:
                if user["id"] == emp_id:
                    emp_name = user["name"]

            print(f"Employee {emp_name} is done with"
                  f" tasks({done_tasks}/{total_tasks}):")
        else:
            print("Error: Unable to fetch data.")

        for item in todo_data:
            if item["completed"]:
                print(f'\t {item["title"]}')
    else:
        print("Error: Unable to fetch data.")


if __name__ == "__main__":
    toDo()
