import random
import csv
from faker import Faker
fake = Faker()

# Generating 1000 rows of data
rows = []
for _ in range(1000):
    name = fake.first_name() + ' ' + fake.last_name()
    department = fake.random_element(elements=('Sales', 'Marketing', 'HR', 'IT'))
    manager = fake.first_name()
    price = random.randint(0, 1000)
    date = fake.date_this_year()
    row = [name, department, manager, f'${price}', date]
    rows.append(row)

# Writing data to a CSV file
with open('generated_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Department', 'Manager', 'Price', 'Date'])
    writer.writerows(rows)

print("Data generated successfully!")
