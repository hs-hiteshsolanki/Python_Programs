import json
import os

import pandas as pd
from openpyxl import load_workbook

customer_table = {
    'database_name': 'Customer Table',
    'struct': {
        "id": {'datatype': "int", 'notNull': True},
        "name": {'datatype': "str", 'notNull': True},
        "age": {'datatype': "int", 'notNull': True},
        "dob": {'datatype': "int", 'notNull': True},
        "number": {'datatype': "int", 'notNull': True},
    },
    'database': []
}

vehicle_table = {
'database_name': 'Vehicle Table',
    'struct': {
        "id": {'datatype': "int", 'notNull': True},
        "number_plate": {'datatype': "int", 'notNull': True},
        "model": {'datatype': "str", 'notNull': True},
        "owner_id": {'datatype': "str", 'notNull': True},
    },
    'database': []
}

bill_table = {
'database_name': 'Bill Table',
    'struct': {
        "id": {'datatype': "int", 'notNull': True},
        "bill_number": {'datatype': "int", 'notNull': False},
        "owner_id": {'datatype': "int", 'notNull': True},
        "price": {'datatype': "int", 'notNull': True},
        "vehicle_id": {'datatype': "int", 'notNull': True},
    },
    'database': []
}

table = {
    "table_list": {
        "customer" : customer_table,
        "vehicle" : vehicle_table,
        "bill" : bill_table,
    },
}
database_file_name = 'garage_management.json'
def write_data():
    with open(database_file_name, 'w+') as f:
        f.write(json.dumps(table))

def load_data():
    with open(database_file_name, "r") as read:
        jsonData = json.load(read)
    return jsonData

def write_database(table):
    with open(database_file_name, 'w') as f:
        f.write(json.dumps(table,indent = 4))

# write_data()
file_name = 'garage_management.xlsx'
def write_database_excel_file(data,sheet_name):
    #data store in json file
    # with open(database_file_name, 'w') as f:
    #     f.write(json.dumps(data,indent = 4))
    # data = pd.DataFrame(data)
    # data.to_excel(file_name)

    #data store in Excel file
    df = pd.DataFrame.from_dict(data)
    # if the file exists
    if not os.path.isfile(file_name):
        with pd.ExcelWriter(file_name, engine="openpyxl", mode="w") as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    else:
        #,startrow= 12,header=False
        with pd.ExcelWriter(file_name, engine='openpyxl', mode='a',if_sheet_exists="overlay") as writer:
            df.to_excel(writer,sheet_name=sheet_name,index=False)
