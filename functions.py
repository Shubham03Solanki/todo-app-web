FILEPATH = "store.txt"


def todos_read(filepath=FILEPATH):
    """ This function reads the given file
    for todos """
    with open(filepath, 'r') as file:
        lists_local = file.readlines()
    return lists_local


def todos_write(lists, filepath=FILEPATH):
    """ This function takes the todos in a list and
    then writes to a mentioned file"""
    with open(filepath, 'w') as file:
        file.writelines(lists)


if __name__ == "__main__":
    print("Hi i am shubham solanki")
    print(__name__)