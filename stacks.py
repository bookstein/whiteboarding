"""Queue class inherits from List
a queue involves popping from the front of the list"""

class Queue (list):
    # pass in variable number of args (your list)
    def __init__(self, *args):
    """init using list object's init, since a queue looks just like a list
    +use SUPER class to denote a reference to list object (parent class)
    from which we're inheriting"""
        super(Queue, self).__init__(*args)
        # super(Queue, self) references list
        # super makes sure to reference whatever the parent class is

    # using list object's pop method, create pop method specific to queue
    def pop(self):
        return super(Queue, self).pop(0)  # removes first item from list

"""Stack: pop from the end (last in first out, LIFO)"""
class Stack(list):
    def __init__(self, *args):
        super(Stack, self).__init__(*args)

    def pop(self):
        return super(Queue, self).pop() #  pops last item

"""but you don't HAVE to write a class for a queue or stack -- just remember to pop off from the front OR the end"""


