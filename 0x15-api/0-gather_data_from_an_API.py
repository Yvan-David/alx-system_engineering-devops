#!/usr/bin/python3
""" takes in a letter and sends a POST request to
to use json file of the response """

import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/todos/"
    r = requests.get(url)
    total_tasks = 0
    done_tasks = 0
    n = int(sys.argv[1])
    content = []

    try:
        json_dict = r.json()
        if json_dict:
            for i in range(1, json_dict.__len__()):
                if json_dict[i].get('userId') == n:
                    total_tasks += 1
                if json_dict[i].get('userId') == n and \
                   json_dict[i].get('completed') is True:
                    done_tasks += 1
                    content.append(json_dict[i].get('title'))
            print(f"Employee {json_dict[n].get('username')}", end='')
            print(f" is done with tasks({done_tasks}/{total_tasks}):")
            for i in content:
                print(f"\t {i}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
