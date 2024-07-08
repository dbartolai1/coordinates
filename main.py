import json
import sys
import os



args = sys.argv

def check_args():
    if len(args) == 2: 
        return args[1]
    if len(args) > 2:
        print('ERROR: Too many args')
    else:
        pass
        #Assume pulling

def push_coords():
    place = str(input('Enter name: '))
    coords = str(input('Enter coords: '))
    with open("data.json", "r") as f:
        data = json.load(f)
    data[place] = coords
    with open("data.json", "w") as f:
        json.dump(data, f)

def new_user():
    username = str(input('Username: '))
    with open('user.json', 'r') as f:
        data = json.load(f)
    data.append(username)
    with open('user.json', 'w') as f:
        json.dump(data, f)


def get_users():
    with open('user.json', 'r') as f:
        data = json.load(f)
    output=[]
    for i in data:
        output.append(i)
    return output

def select_user():
    users = get_users()
    for i in range(len(users)):
        print(f'{i}: {users[i]}')
    x = input('Select user: ')
    return users[i]

def pull_coords(user):
    arg = str(input('Location: '))
    with open("data.json", "r") as f:
        data = json.load(f)
    for i in data.keys():
        if i == arg:
            command = f'tp {user} {data[i]}'
            copy(command)

def copy(text):
    os.system(f'echo "{text}" | pbcopy')
            

def main():
    arg = check_args()

    if arg == 'load':
        push_coords()
    elif arg == 'user':
        new_user()
    else:
        user = select_user()
        pull_coords(user)


main()