# import sys to receive arguments from the command line
import sys
# import other modules defined in the project
from Utils.mathematical_functions import sum
from Entities.Client import Client

a, b = sys.argv[1:]
print(sum(int(a), int(b)))

# Autocomplete the below line with email password and client id
client = Client('John', 'Doe', 30, 'Calle 1', '123456789', 'john@doe.com', '123', '1')
client.greet()