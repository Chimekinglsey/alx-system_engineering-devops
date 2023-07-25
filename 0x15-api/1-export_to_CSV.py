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

    userId = ""
    userName = ""
    task_status = ""
    task_title = ""

    for user in users:
        if emp_id == user['id']:
            userName = user['username']
            break

    for task in todo:
        if emp_id == task['userId']:
            userId = task['userId']
            task_status = str(task['completed'])
            task_title = task['title']

            with open(USER_ID.csv, 'a') as w:
                w.write(f'"{userId}","{userName}","{task_status}",\
"{task_title}"\n')
