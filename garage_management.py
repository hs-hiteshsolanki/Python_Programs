import os
import json
from file_create import load_data, write_database


def database_select():
    os.system('clear')
    while True:
        print("""Please select database!
        1. customer table
        2. data in vehicle table
        3. data in bill table
        4. Exit
        """)

        choise = int(input("enter a key for select database : "))
        if choise == 1:
            data = load_data()
            # print(data['table_list']['customer'])
            return data['table_list']['customer']
        elif choise == 2:
            # return vehicle_table
            data = load_data()
            return data['table_list']['vehicle']
        elif choise == 3:
            data = load_data()
            return data['table_list']['bill']
            # return bill_table
        elif choise == 4:
            print("Exiting Program")
            break
        else:
            print("Not a valid Input")
            break

def display_data(table):
    os.system('clear')
    print(f"database table structure is {table['struct']}")

    if not table['database']:
        print("No found record in database")
        if not table['database']:
            data_store_or_not = input("Enter a data in database Choose Yes or No : ")
            data_store_or_not = data_store_or_not.lower().strip()
            if data_store_or_not == "yes":
                return insertData(table)
            else:
                print("No found record in database")

    for index,value in enumerate(table['database']):
        print(f"{index}:{value}")
    print()

def insertData(table):
    os.system('clear')
    print(f"inserting row for {table['database_name']} database")
    row = {}
    structure = table['struct']
    for key in structure.keys():
        while True:
            userInput = input(f"{key} : ")
            if structure[key].get('notNull', False):
                if not userInput:
                    print(f"{key} is a required field")
                    continue
            else:
                row[key] = ""
                break
            datatype = structure[key].get('datatype', 'str')
            if datatype == 'int':
                if not isinstance(int(userInput), int):
                    print(f"{key} is a not correct datatype")
                    continue
            else:
                if not isinstance(userInput, str):
                    print(f"{key} is a not correct datatype")
                    continue
            # if not isinstance(userInput, datatype):
            #     print(f"{key} is a not correct datatype")
            #     continue
            if datatype == 'int':
                row[key] = int(userInput)
            else:
                row[key] = userInput
            break

    data = table['database'].append(row)
    print(data)
    # with open('database_list.json', 'a') as f:
    #     f.write(json.dumps(data))
    display_data(table)
    # write_database(data)
    # return data

def data_delete(table):
    os.system('clear')
    display_data(table)

    delete_item = int(input("Enter a Delete Item : "))
    for row_id, row in enumerate(table['database']):
        if row['id'] == delete_item:
            del table['database'][row_id]
            print(row)
            break
        else:
            print("Entered key is not valid")

def select_record(table):
    os.system('clear')
    display_data(table)

    select_record_key = int(input("Enter a select record key : "))
    for row in table['database']:
        if row['id'] == select_record_key:
            print(row)
        else:
            print("Entered key is not valid")

def update_record(table):
    os.system('clear')
    display_data(table)
    print(f"updating row for {table['database_name']} database")

    select_record_key = int(input("Enter a select record key : "))
    for row_id, row in enumerate(table['database']):
        if row['id'] == select_record_key:
            update_data = {}
            structure = table['struct']
            for key in structure.keys():
                while True:
                    userInput = input(f"{key} : ")
                    if structure[key].get('notNull', False):
                        if not userInput:
                            print(f"{key} is a required field")
                            continue
                    else:
                        update_data[key] = ""
                        break
                    datatype = structure[key].get('datatype', 'str')
                    if datatype == 'int':
                        if not isinstance(int(userInput), int):
                            print(f"{key} is a not correct datatype")
                            continue
                    else:
                        if not isinstance(userInput, str):
                            print(f"{key} is a not correct datatype")
                            continue
                    # if not isinstance(userInput, datatype):
                    #     print(f"{key} is a not correct datatype")
                    #     continue
                    if datatype == 'int':
                        update_data[key] = int(userInput)
                    else:
                        update_data[key] = userInput
                    break

            table['database'][row_id] = update_data
        else:
            print("Entered key is not valid")

while True:
    os.system('clear')
    print("""Welcome to my Garage!
    perform task in Garage database
    1. display all record
    2. select record
    3. insert record
    4. update record
    5. delete record
    6. Exit
    """)

    databaseTask = int(input("enter a key : "))
    if databaseTask == 1:
        table = database_select()
        display_data(table)
    elif databaseTask == 2:
        table = database_select()
        select_record(table)
    elif databaseTask == 3:
        table = database_select()
        insertData(table)
    elif databaseTask == 4:
        table = database_select()
        update_record(table)
    elif databaseTask == 5:
        table = database_select()
        data_delete(table)
    elif databaseTask == 6:
        print("Exiting Program")
        break
    else:
        print("Not a valid Input")


