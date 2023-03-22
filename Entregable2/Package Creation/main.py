# import sys to receive arguments from the command line
import sys
# import other modules defined in the project
from ecommerce.Client import Client

# Test that package import works
a, b = sys.argv[1:]
print(sum(int(a), int(b)))

# Create a Client
client = Client('John', 'Doe', 30, 'Calle 1', '123456789', 'john@doe.com', '123', '1')
client.greet()