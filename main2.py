from pathlib import Path
import json
"""
numbers = [2, 3, 5, 7, 11, 13]
path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)

numbers1 = json.loads(contents)
print(numbers1)
"""


"""
username = input('What is your name: \n')

path = Path('usernames.json')
contents = json.dumps(username)
path.write_text(contents)
username = json.loads(contents)
print(username)

#print(f"We'll remember you when you come back, {username}!")
"""


"""
path = Path('usernames.json')
if path.exists():
    contents = path.read_text()
    usernames = json.loads(contents)
    print(f"Welcome back, {usernames}!")

else:
    username = input('What is your name: \n')
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")
"""


def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    username = input('What is your name: \n')
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()

"""
def greet_user():
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        usernames = json.loads(contents)
        print(f"Welcome back, {usernames}!")

    else:
        username = input('What is your name: \n')
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
    """