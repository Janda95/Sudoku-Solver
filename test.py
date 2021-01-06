#! python3

'''
python3 -m venv ~/venv3
pip install opencv-python absl-py
'''

from absl import app
from absl import flags

import numpy as np

Flags = flags.FLAGS

# (flagName, defaultValue, descriptionString)
flags.DEFINE_list("myList", [], "list test")
flags.DEFINE_string('myString', 'Hello World', 'string test')
flags.DEFINE_integer('myInt', -1, 'integer test')


def main(argv):
	print("Hello World")
	print(argv)
	for item in argv:
		print(item)
	
	print(str(Flags.myList))
	print(str(Flags.myString))
	print(str(Flags.myInt))


if __name__ == '__main__':
	app.run(main)

