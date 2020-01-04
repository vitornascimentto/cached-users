import sys

def get_username ():
    if len(sys.argv) != 3 and sys.argv[1] != "-username":
        return 'Error: formato de entrada invalido. (Ex: python3 cached_users.py -username Samantha)'

    return sys.argv[2]
