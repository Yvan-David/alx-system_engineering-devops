#!/usr/bin/python3
""" takes in a letter and sends a POST request to
to use json file of the response """

import requests
import sys
import csv

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/todos/"
    r = requests.get(url)
    content = []
    n = int(sys.argv[1])
    name = sys.argv[1] + '.csv'
    try:
        json_dict = r.json()
        if json_dict:
            for i in range(1, json_dict.__len__()):
                if json_dict[i].get('userId') == n:
                    a = '\'\'' + str(n) + '\'\''
                    b = '\'\'' + str(json_dict[n].get('username')) + '\'\''
                    c = '\'\'' + str(json_dict[i].get('completed')) + '\'\''
                    d = '\'\'' + str(json_dict[i].get('title')) + '\'\''
                    with open(name, 'a+', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([a, b, c, d])
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
