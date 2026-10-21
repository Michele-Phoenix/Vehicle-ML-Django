import csv
import random

manufacturers = ['Toyota', 'Honda', 'Ford', 'Tesla', 'BMW', 'Mercedes']

with open('dummy_data/vehicles_data_1000.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['manufacturer', 'model', 'year'])
    for i in range(1000):
        writer.writerow([
            random.choice(manufacturers),
            f'Model {i}',
            random.randint(2010, 2024)
        ])
