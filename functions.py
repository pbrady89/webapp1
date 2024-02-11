FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """This function is used to read the saved to-do list"""
    with open(filepath, 'r') as save:
        todos_local = save.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write to-do items list to the text file"""
    with open(filepath, 'w') as save:
        save.writelines(todos_arg)


def extract(feet_inches):
    imperial_list = feet_inches.split(' ')
    inches_local = float(imperial_list[1])
    feet_local = float(imperial_list[0])
    return {'feet': feet_local, 'inches': inches_local}


def convert(feet, inches):
    total_feet = inches / 12 + feet
    meters_local = total_feet * 0.3048
    return meters_local
