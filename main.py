from utils import get_username, request_username

if __name__ == "__main__":

    CSV = 'cached.csv'
    URL = 'https://jsonplaceholder.typicode.com/users'
    USERNAME = get_username()

    response_api = request_username(USERNAME, URL, CSV)
    print(f'API: {response_api}')
