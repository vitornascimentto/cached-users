from utils import get_username, request_username, username_already_exist

if __name__ == "__main__":

    CSV = 'cached.csv'
    URL = 'https://jsonplaceholder.typicode.com/users'
    USERNAME = get_username()

    exist = username_already_exist(CSV, USERNAME)
    
    if exist: 
        print(f'CACHED: {exist}')
    else:
        request_api = request_username(USERNAME, URL, CSV)
        print(f'API: {request_api}')
