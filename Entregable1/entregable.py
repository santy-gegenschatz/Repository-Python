import time

class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def __str__(self):
        return f'{self.username}, {self.password}'

class Server():
    def __init__(self, users):
        self.users = users or []

    def login(self, username, password):
        try:
            for user in self.users:
                if (user.username == username):
                    if (user.password == password):
                        return f'Welcome to the server {username}'
                    else:
                        return f'The password is incorrect'
            return f'There is no user with the username {username}'
        except:
            # In this case the users array is empty
            return 'There are no users in the system yet'
    
    def signup(self, username, password):
        try:
            for user in self.users:
                if (username == user.username):
                    return f'The username {username} is already taken'
            new_user = User(username, password)
            self.users.append(new_user)
            return f'The user {username} has been successfully created'
        except:
            # In this case this is the first user to be created
            new_user = User(username, password)
            self.users.append(new_user)
            return f'The user {username} has been successfully created'

    def save_data(self, database_name):
        with open(f'{database_name}.txt', 'w') as file:
            file.write('Users\n')
            if self.users is not None:
                for item in self.users:
                    file.write(f"{item}\n")


    def read_data(self, database_name):
        print('Loading Database')
        try:
            with open(f'{database_name}.txt', 'r') as file:
                self.users = []
                for index, line in enumerate(file.readlines()):
                    if (index is not 0):
                        username = line.split()[0].split(',')[0]
                        password = line.split()[1]
                        new_user = User(username, password)
                        print(f'Loading user {index}')
                        self.users.append(new_user)
        except:
            print('Database not found')


    def start(self):
        self.read_data('database')
        run = True
        while run:
            action = input('Press L to login, S to signup, E to exit ')
            if (action == 'L' or action == 'S'):
                username = input('Enter your username: ')
                password = input('Enter your password: ')
                if (action == 'L'):
                    print(self.login(username, password))
                else:
                    print(self.signup(username, password))
            elif (action == 'E'):
                print('Exiting program')
                print('Saving data to text File')
                self.save_data('database')
                time.sleep(1)
                run = False
            else:
                print('Command not recognized, please try again')

server = Server(None)
server.start()
                
