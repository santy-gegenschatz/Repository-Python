class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def __str__(self):
        return f'{self.username}, {self.password}'

class Server():
    def __init__(self, usuarios):
        self.usuarios = usuarios

    def login(self, username, password):
        try:
            for user in self.usuarios:
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
            for user in self.usuarios:
                if (username == user.username):
                    return f'The username {username} is already taken'
            new_user = User(username, password)
            self.usuarios.append(new_user)
            return f'The user {username} has been successfully created'
        except:
            # In this case this is the first user to be created
            self.usuarios = []
            new_user = User(username, password)
            self.usuarios.append(new_user)
            return f'The user {username} has been successfully created'

    def save_data(self, database_name):
        with open(f'{database_name}.txt', 'w') as file:
            for item in self.usuarios:
                file.write(f"{item}\n")

    def start(self):
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
                run = False
            else:
                print('Command not recognized, please try again')

server = Server(None)
server.start()
                
