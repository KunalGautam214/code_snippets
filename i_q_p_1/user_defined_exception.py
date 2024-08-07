# Write a program of user defined exception in python

class UserDefinedException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


try:
    list_items = [1, 2, -1, 10, 11]
    for item in list_items:
        if item >= 0:
            print(item)
        else:
            try:
                raise UserDefinedException('Value is less than zero ' + str(item))
            except UserDefinedException as e:
                print(e)
except Exception as e:
    print(e)
