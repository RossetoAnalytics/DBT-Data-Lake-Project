import csv
import os
from faker import Faker
import random

# Create Faker instance for pt_BR locale
fake = Faker('pt_BR')

# Path to the Downloads folder
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# Number of records to generate
num_records = 100
num_records_sales = 2000

# Generate 'unidades' data
unidades_file = os.path.join(downloads_folder, 'unidades.csv')
unit_ids = []
with open(unidades_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['unit_id', 'unit_name', 'city'])

    for _ in range(num_records):
        unit_id = fake.unique.random_number(digits=4)
        unit_ids.append(unit_id)
        writer.writerow([
            unit_id,
            fake.company(),
            fake.city()
        ])

# Generate 'produtos' data
produtos_file = os.path.join(downloads_folder, 'produtos.csv')
product_ids = []
with open(produtos_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['product_id', 'name', 'price', 'description'])

    for _ in range(num_records):
        product_id = fake.unique.random_number(digits=5)
        product_ids.append(product_id)
        writer.writerow([
            product_id,
            fake.word(),
            round(random.uniform(10.0, 1000.0), 2),  # Preço aleatório
            fake.text(max_nb_chars=50)
        ])

# Generate 'clientes' data
clientes_file = os.path.join(downloads_folder, 'clientes.csv')
customer_ids = []
with open(clientes_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['customer_id', 'unit_id', 'name', 'address', 'phone', 'email'])

    for _ in range(num_records):
        customer_id = fake.unique.random_number(digits=6)
        customer_ids.append(customer_id)
        writer.writerow([
            customer_id,
            random.choice(unit_ids),  # Randomly assign a unit_id
            fake.name(),
            fake.address(),
            fake.phone_number(),
            fake.email()
        ])

# Generate 'vendedores' data
vendedores_file = os.path.join(downloads_folder, 'vendedores.csv')
vendor_ids = []
with open(vendedores_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['vendor_id', 'name', 'email'])

    for _ in range(num_records):
        vendor_id = fake.unique.random_number(digits=5)
        vendor_ids.append(vendor_id)
        writer.writerow([
            vendor_id,
            fake.name(),
            fake.email()
        ])

# Generate 'vendas' data
vendas_file = os.path.join(downloads_folder, 'vendas.csv')
with open(vendas_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['purchase_id', 'customer_id', 'vendor_id', 'unit_id', 'product_id', 'date', 'quantity', 'discount',
                     'store_type', 'payment_method'])

    for _ in range(num_records_sales):
        writer.writerow([
            fake.unique.random_number(digits=7),
            random.choice(customer_ids),  # Randomly assign a customer_id
            random.choice(vendor_ids),  # Randomly assign a vendor_id
            random.choice(unit_ids),  # Randomly assign a unit_id
            random.choice(product_ids),  # Randomly assign a product_id
            fake.date_this_year(),
            random.randint(1, 10),  # Random quantity between 1 and 10
            round(random.uniform(0, 50.0), 2),  # Random discount
            random.choice(['Online', 'In-Store']),  # Store type
            random.choice(['Cartão de Crédito', 'Dinheiro', 'Transferência'])  # Payment method
        ])

print("Arquivos CSV gerados na pasta Downloads com sucesso!")
