# 1 importing statements

from faker import Faker

# 2 initialising the package

fake = Faker()

# 3 Generating random name

name = "Name: " + fake.name()+ "\n"

# 4 Generating random address

address = "Address: " + fake.address()

# 5 Displayong the generated name and address

print(name,address)