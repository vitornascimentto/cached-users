import sys
import requests
import os

def get_username ():
    if len(sys.argv) != 3 and sys.argv[1] != "-username":
        return 'Error: formato de entrada invalido. (Ex: python3 cached_users.py -username Samantha)'

    return sys.argv[2]

def username_already_exist (csv, username):
    with open('cached.csv', 'r') as csv:
        content = csv.readlines()

        for i in content:
            data_split = i.split(',') 

            if username in data_split:
                return_result = {'email': data_split[1], 'website': data_split[2], 'hemisferio': data_split[3][:3:]}
                return return_result

        return False

def request_username (username, url, csv):
    params = {'username': username}

    api = requests.get(url, params=params)

    result = api.json()[0]

    if float(result['address']['geo']['lat']) < 0:
        result['hemisferio'] = 'sul'
    else:
        result['hemisferio'] = 'norte'

    if os.path.getsize('cached.csv') == 0:
        with open('cached.csv', 'w') as csv:
            csv.write('username,email,website,hemisferio\n')

    if os.path.getsize('cached.csv') > 0:
        with open('cached.csv', 'r') as csv:
            
            csv = csv.readlines()

            csv.append(f"{result['username']},{result['email']},{result['website']},{result['hemisferio']}\n")
            
            with open('cached.csv', 'w') as arq:
                arq.writelines(csv)

    return_result = {'email': result['email'], 'website': result['website'], 'hemisferio': result['hemisferio']}

    return return_result