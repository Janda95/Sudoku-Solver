'''
Goal:

Assist in Randomizing Scene for Teleop Data Collection


Params:
Size of Surface:
w x h --> (x, y)

Number of objects:
n


Installation instructions:

python3 -m venv ~/venv3
pip install opencv-python absl-py


How to run:
python3 item_randomization.py --total_objects=<int> --width=<int> --height=<int>

NOTE:
Height and Width are arbitrary, you could use a distance measurement or divide your test space into chunks.
Do what works for you!
'''

from absl import app
from absl import flags

import random

#flags.DEFINE_integer('flag_name', defaultValue, 'descriptor' )

flags.DEFINE_integer('total_objects', None, 'number of objects')
flags.DEFINE_integer('height', None, 'max height constraint')
flags.DEFINE_integer('width', None, 'max width constraint')
#flags.DEFINE_boolean('stackable', True, 'Can objects share same locations')

FLAGS = flags.FLAGS

USAGE = """
"""

# check for valid number 1 or more, return -1 if false
def is_valid_number(num_string):
    isValid = False

    try:
        num = int(num_string)
    except ValueError:
        msg = "Error: " + num_string + " is Invalid Integer! \n" 
        print(msg)
        return -1

    if num < 1:
        msg = "Error: " + num_string + " needs to be 1 or greater \n"
        print()
        return -1

    return num


def pretty_print_mylist(location_list):
    print("\nLocation for each item: \n")
    i = 0
    for item in location_list:
        i += 1
        msg = str(i) + ": (" + str(item[0]) + ", " + str(item[1]) + ") --- deg: " + str(item[2])

        print(msg + "\n")


def main(argv):
    # validate
    h = FLAGS.height
    w = FLAGS.width
    n = FLAGS.total_objects

    #saved_locations = dict()
    item_locations = list()

    while(h == None or h < 1):
        val = input("Height > 1: ")
        h = is_valid_number(val)

    while(w == None or w < 1):
        val = input("Width > 1: ")
        w = is_valid_number(val)

    while(n == None or n < 1):
        val = input("Total objects > 1 ")
        n = is_valid_number(val)

    for i in range(0, n):
        # rand number between 1 - h, 1 - w, 0 - 364
        x = random.randrange(1, w+1, 1)
        y = random.randrange(1, h+1, 1)
        deg = random.randrange(0, 365, 1)

        # dictionary usage
        location = x, y

        # general location data
        item_data =  [x, y, deg]
        item_locations.append(item_data)
    
    pretty_print_mylist(item_locations)


if __name__ == "__main__":
    app.run(main)
