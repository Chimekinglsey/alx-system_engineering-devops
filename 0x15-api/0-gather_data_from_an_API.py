#!/usr/bin/python3
"""
0. Gather data from an API
"""

import requests
import sys

if __name__ == '__main__':
    emp_id = int(sys.argv[1])
    todo = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    tasks_completed = 0
    total_tasks = 0
    emp_name = None
    task_title = []
    for user in todo:
        if user['userId'] == emp_id:
            total_tasks += 1
    
    for user in todo:
        if user['userId'] == emp_id and user['completed'] == True:
            tasks_completed += 1
            task_title.append(user['title'])
    
    # for name in users:
    #     if name['id'] == emp_id:
    #         emp_name = name['name']
    print(f'Employee {emp_name} is done with tasks\
({tasks_completed}/{total_tasks}):')
    for item in task_title:
        print(f"\t {item}")
