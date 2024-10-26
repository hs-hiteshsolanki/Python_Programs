import os
import click
from file_create import load_data, write_database, write_database_excel_file

all_tables = load_data()
customer_table = all_tables['table_list']['customer']
vehicle_table = all_tables['table_list']['vehicle']
bill_table = all_tables['table_list']['bill']

def database_select():
    os.system('clear')
    while True:
        print("""Please select database!
        1. customer table
        2. vehicle table
        3. bill table
        4. Exit
        """)

        choise = int(input("enter a key for select database : "))
        if choise == 1:
            # print(data['table_list']['customer'])
            return customer_table
        elif choise == 2:
            return vehicle_table
        elif choise == 3:
            return bill_table
        elif choise == 4:
            break
        else:
            print("Not a valid Input")

def display_data(table):
    os.system('clear')
    print(f"database table structure is {table['struct']}")

    if not table['database']:
        print("No found record in database")
        return False
    else:
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

    table['database'].append(row)
    display_data(table)
    return table

def data_delete(table):
    os.system('clear')
    display_data(table)
    if display_data(table) != False:
        delete_item = int(input("Enter a Delete record id : "))
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
    if display_data(table) != False:
        select_record_key = int(input("Enter a Select record id : "))
        for row in table['database']:
            if row['id'] == select_record_key:
                print(row)
            else:
                print("Entered key is not valid")

def update_record(table):
    os.system('clear')
    display_data(table)

    print(f"updating row for {table['database_name']} database")
    if display_data(table) != False:

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
    else:
        print("No found record in database")

while True:
    print("""Welcome to my Garage!
    perform task in Garage database
    1. display all record
    2. select record
    3. insert record
    4. update record
    5. delete record
    6. Exit
    """)

    # select_opration = input("enter a key : ")
    select_opration = click.prompt("enter a key ",type=int)

    # if not isinstance(select_opration, int):
    #     print("Not a valid Input")
    #     continue
    #
    # select_opration= int(select_opration)
    if select_opration == 1:
        table = database_select()
        display_data(table)
        continue
    elif select_opration == 2:
        table = database_select()
        select_record(table)
        continue
    elif select_opration == 3:
        table = database_select()
        data = insertData(table)
        write_database_excel_file(table['database'],table['database_name'])
        continue
    elif select_opration == 4:
        table = database_select()
        update_record(table)
        continue
    elif select_opration == 5:
        table = database_select()
        data_delete(table)
        continue
    elif select_opration == 6:
        break
    else:
        print("Not a valid Input")

os.system('clear')







