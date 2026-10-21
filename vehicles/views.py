import csv
from django.shortcuts import render
from .dashboard import get_frequency_table

def dashboard_view(request):
    data_list = []
    with open("dummy_data/vehicles_data_1000.csv", mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data_list.append(row)
            
    context = {
        "manufacturer_table": get_frequency_table(data_list, 'manufacturer', 'Manufacturer'),
        "body_type_table": get_frequency_table(data_list, 'body_type', 'Body Type'),
        "fuel_type_table": get_frequency_table(data_list, 'fuel_type', 'Fuel Type'),
        "transmission_table": get_frequency_table(data_list, 'transmission', 'Transmission'),
        "condition_table": get_frequency_table(data_list, 'vehicle_condition', 'Condition'),
        "continent_table": get_frequency_table(data_list, 'client_continent', 'Client Continent'),
    }
    return render(request, "vehicles/index.html", context)
