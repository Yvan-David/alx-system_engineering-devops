#!/usr/bin/python3
""" takes in a letter and sends a POST request to
to use json file of the response """
import json
import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/todos/"
    r = requests.get(url)
    name = 'todo_all_employees.json'
    content = {}
    arr = []
    values = {}
    all = {}

    try:
        json_dict = r.json()
        if json_dict:
            for j in range(1, 11):
                content[json_dict[j].get('userId')] = arr
                for i in range(1, json_dict.__len__()):
                    if json_dict[i].get('userId') == j:
                        values["task"] = json_dict[i].get('title')
                        values["completed"] = json_dict[i].get('completed')
                        values["username"] = json_dict[j].get('username')
                        arr.append(values)
                arr_1 = arr
            with open(name, 'a+', newline='') as file:
                json.dump(content, file)
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
