#!/usr/bin/python3
""" This script uses REST API to retrieve the task completed
    by a given employee ID, then exports it to a json file """

import json
import requests
from sys import argv


def toDo():
    """ Function exports todo list to a json file """
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
                    usr_name = user["username"]
        else:
            print("Error: Unable to fetch data.")

        todo_list = []
        for item in todo_data:
            todo_list.append({
                "task": item['title'],
                "completed": item['completed'],
                "username": usr_name
            })

        todo_dict = {emp_id: todo_list}

        with open(f'{emp_id}.json', mode='w', newline='') as file:
            json.dump(todo_dict, file)

    else:
        print("Error: Unable to fetch data.")


if __name__ == "__main__":
    toDo()
